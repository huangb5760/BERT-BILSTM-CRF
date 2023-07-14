# coding: utf-8
# flask + gevent + multiprocess + wsgi

from gevent import monkey
from gevent.pywsgi import WSGIServer
monkey.patch_all()

import datetime
import os
from multiprocessing import cpu_count, Process
from flask import Flask, jsonify
import json
from flask import request
from predict import  Predictor
import time


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

@app.route("/extraction", methods=["POST"])
def extract_data():
    if request.method == "POST":
        params = request.get_json()
        text = params["text"]
        if not text:
            return json.dumps({"msg": "输入的文本为空",
                               "ucode": 404,
                               "result": {}
                               }, ensure_ascii=False)
        # 抽取关联信息
        try:
            start = time.time()
            ner_result = predictor.ner_predict(text)
            end = time.time()
            print("耗时：{}s".format(end - start))
        except Exception as e:
            logger.error(ner_result)
            logger.error(e)
            return json.dumps({"msg": e,
                               "ucode": 500,
                               "result": {}
                               }, ensure_ascii=False)
        return json.dumps({"msg": "success",
                           "ucode": 200,
                           "result": ner_result
                           }, ensure_ascii=False)
    else:
        return json.dumps({"msg": "请求方式为post",
                           "ucode": 500,
                           "result": {}
                           }, ensure_ascii=False)

class ReturnResult:
    def __init__(self, msg=None, result=None, ucode=None):
        self.msg = msg
        self.result = result
        self.ucode = ucode

def run(MULTI_PROCESS):
    if MULTI_PROCESS == False:
        WSGIServer(('0.0.0.0', 8080), app).serve_forever()
    else:
        mulserver = WSGIServer(('0.0.0.0', 8080), app)
        mulserver.start()

        def server_forever():
            mulserver.start_accepting()
            mulserver._stop_event.wait()

        for i in range(cpu_count()):
            p = Process(target=server_forever)
            p.start()

if __name__ == "__main__":
    predictor = Predictor('steel')
    # 单进程 + 协程
    run(False)
    # 多进程 + 协程
    # run(True)
