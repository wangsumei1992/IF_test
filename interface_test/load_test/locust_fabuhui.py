from locust import HttpLocust, TaskSet, task
import locust.stats
locust.stats.CSV_STATS_INTERVAL_SEC = 5  #设置数据采集频率

# web性能测试
class UserBehavior(TaskSet):

    def on_start(self):
        """on_start is called when a Locust start before any task is scheduled"""
        self.login()

    def login(self):
        self.client.post("/", {"username":"admin","password":"admin123456"})

    @task(2)
    def event_manage(self):
        self.client.get("/event_manager/")

    @task(2)
    def guest_manage(self):
        self.client.get("/guest_manage/")

    @task(1)
    def search_phone(self):
        self.client.get("/guest_manage/guest_name/",params={"event_name":"apd"})

class WebsiteUser(HttpLocust):
    weight = 3  #设置执行权重
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000

class APPsiteUser(HttpLocust):
    weight = 5  #设置执行权重
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000