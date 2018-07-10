from locust import HttpLocust, TaskSet, task
import locust.stats
locust.stats.CSV_STATS_INTERVAL_SEC = 5  #设置数据采集频率

#定义用户行为
class UserBehavior(TaskSet):

    @task
    def baidu_page(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):

    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000

