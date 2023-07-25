import json
from flask import Flask
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


if __name__ == '__main__':
    predictor = Predictor('steel')
    app.run(host="0.0.0.0", port=9277, debug=False, threaded=3)
# 启动 nohup python -u server.py > nohup.log &
# 访问 curl  http://10.80.92.7:9277/extraction -X POST -d '{"text": "1.4*1250*2500 1.8*1250*2500本钢盒板什么价格呢"}' --header "Content-Type: application/json"