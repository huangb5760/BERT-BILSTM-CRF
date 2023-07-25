from locust import HttpUser, TaskSet, task
import json
class WebsiteTasks(TaskSet):
    
    #def on_start(self):
    #    self.client.post("/login", { "username": "test", "password": "123456" })

    @task(1)
    def extraction1(self):
        data = json.dumps({ "text": "1.4*1250*2500 1.8*1250*2500本钢盒板什么价格呢" })
        headers = {"Content-Type": "application/json"}
        self.client.post("/extraction",data,headers=headers)

    @task(1)
    def extraction2(self):
        headers = {"Content-Type": "application/json"}
        data = json.dumps({ "text": "花纹2.75*1250  3.75*1250  4.75*1250  5.75*1250  普卷2.75*1250  3.75*1250  5.75*1250  7.75*1250  9.75*1250  13.75*1500  15.5*1500  15*1500的有么" })
        self.client.post("/extraction",data,headers=headers)

    @task(1)
    def extraction3(self):
        headers = {"Content-Type": "application/json"}
        data = json.dumps({ "text": "求购：SPHC4.0*1500。SPHC6.0*1500各一枚" })
        self.client.post("/extraction",data,headers=headers)

    @task(1)
    def extraction4(self):
        headers = {"Content-Type": "application/json"}
        data = json.dumps({ "text": "11.75*1500*6000的8张 13.75*1500*6000的6张" })
        self.client.post("/extraction",data,headers=headers)

    @task(1)
    def extraction5(self):
        headers = {"Content-Type": "application/json"}
        data = json.dumps({ "text": "低合金卷5.75*1800  普卷11.3或11.5*1800  普卷1.8*1250 2*1250" })
        self.client.post("/extraction",data,headers=headers)

    tasks = {extraction1: 1, extraction2: 1,extraction3: 1,extraction4: 1,extraction5: 1} # 与装饰器效果一致

class WebsiteUser(HttpUser):
    # task_set = WebsiteTasks  # Usage of User.task_set is deprecated since version 1.0. Set the tasks attribute instead (tasks = [WebsiteTasks])
    tasks = [WebsiteTasks]
    host = "http://tctgpu.zhaogangren.com:9277"
    min_wait = 50
    max_wait = 100