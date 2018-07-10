import unittest, requests, os, sys, json,logging
from parameterized import parameterized

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function/")
sys.path.append(dir + "/data_configuration/")
from get_token import get_stampToken, get_chekToken, get_loginpass, get_auth_token
from get_data import GetData
from datetime import datetime

class ProjectInfoTest(unittest.TestCase):
    url = GetData.url
    def setUp(self):
        self.base_url = self.url + "/project/infonew/"

    # @parameterized.expand([('test_qi', 'WEB', '2',12934, '祥龙抬头测试180205_052','24个月',150000.0,'1111','','2018-02-05',
    #                         '2018-04-01','2018年04月01日'),
    #                        ])
    # def test_project(self, name, source, pages, projectId, projectName,financingDesc, amount,purpose,signAddr,allowInvestAt,
    #                  bidCompletedTime,intdate):
    #     """未登录WEB标的详情"""
    #    # auth_token = get_auth_token("c2446993", "15458524695")
    #     data={'projectId':projectId, 'source':source,'pages':pages}
    #     r = requests.request('get', url=self.base_url+str(data['projectId']),params=data)
    #     print(self.base_url+str(data['projectId']))
    #     result = r.json()
    #     print(result)
    #     print(result['item']['list']['project']['projectID'])
    #     print(result['item']['list']['project']['projectName'])
    #     self.assertEqual(result['item']['list']['project']['projectID'],projectId)
    #     self.assertEqual(result['item']['list']['project']['projectName'], projectName)
    #     # 借款期限
    #     self.assertEqual(result['item']['list']['project']['financingDesc'], financingDesc)
    #     # 借款金额
    #     self.assertEqual(result['item']['list']['project']['amount'], amount)
    #     # 资金用途
    #     self.assertEqual(result['item']['list']['project']['purpose'], purpose)
    #     # 签约地点
    #     self.assertEqual(result['item']['list']['project']['signAddr'], signAddr)
    #     # 募集开始
    #     start_time = datetime.fromtimestamp(result['item']['list']['project']['allowInvestAt']/1000).strftime("%Y-%m-%d")
    #     self.assertEqual(start_time, allowInvestAt)
    #     # 募集完成
    #     end_time = datetime.fromtimestamp(result['item']['list']['project']['bidCompletedTime'] / 1000).strftime("%Y-%m-%d")
    #     self.assertEqual(end_time, bidCompletedTime)
    #     # 起息日
    #     self.assertEqual(result['item']['list']['project']['intdate'], intdate)
    #     intdate
        # self.assertEqual(result['item']['list']['project']['projectID'], projectId)
        # self.assertEqual(result['item']['list']['project']['projectName'], projectName)

    # @parameterized.expand([('name', 'source', 'pages', 'projectId(int)', 'projectName','purpose','amount(int)','(int)financingMaturity',
    #                         'signAddr','allowInvestAt-11-27','bidCompletedTime','intdate','minBidAmount','repaymentCalcTypeDesc',
    #                         ),
    #                        ])
    # def test_project(self, name, source, pages, projectId, projectName,purpose,amount,financingMaturity,signAddr,
    #                  allowInvestAt,bidCompletedTime,intdate,minBidAmount,repaymentCalcTypeDesc):
    #     """未登录APP标的详情"""
    #     #auth_token = get_auth_token("c2446993", "15458524695")
    #     data = {'projectId': projectId, 'source': source, 'pages': '2'}
    #     r = requests.request('get', url=self.base_url + str(data['projectId']), params=data)
    #     print(self.base_url + str(data['projectId']))
    #     result = r.json()
    #     print(result)
    #     print(result['data']['project']['projectID'])
    #     print(result['data']['project']['projectName'])
    #     self.assertEqual(result['data']['project']['projectID'], projectId)
    #     self.assertEqual(result['data']['project']['projectName'], projectName)
    #     # 借款用途
    #     self.assertEqual(result['data']['project']['purpose'], purpose)
    #     # 借款金额
    #     self.assertEqual(result['data']['project']['amount'], amount)
    #     # 借款期限
    #     self.assertEqual(result['data']['project']['financingMaturity'], financingMaturity)
    #     # 签约地点
    #     self.assertEqual(result['data']['project']['signAddr'], signAddr)
    #     # 募集开始
    #     start_time = datetime.fromtimestamp(result['data']['project']['allowInvestAt']/1000).strftime("%Y-%m-%d")
    #     self.assertEqual(start_time, allowInvestAt)
    #     # 募集完成
    #     end_time = datetime.fromtimestamp(result['data']['project']['bidCompletedTime'] / 1000).strftime("%Y-%m-%d")
    #     self.assertEqual(end_time, bidCompletedTime)
    #     # 起息日
    #     self.assertEqual(result['data']['project']['intdate'], intdate)
    #     # 出借金额（最小出借）
    #     self.assertEqual(result['data']['project']['minBidAmount'], minBidAmount)
    #     # 还款方式
    #     self.assertEqual(result['data']['project']['repaymentCalcTypeDesc'], repaymentCalcTypeDesc)
    #     # 还款方式计算公式
    @parameterized.expand([('test_xin',60500,'APP'),
                           #('test_che', 60503, 'APP'),
                           # ('test_qi', 60506, 'APP'),
                           # ('test_fang', 60502, 'APP'),
                           ])
    def test_project(self,name,projectId,source):
        """未登录APP标的详情信息完善"""
        #auth_token = get_auth_token("c2446993", "15458524695")
        data = {'projectId': projectId, 'source': source, 'pages': '2'}
        r = requests.request('get', url=self.base_url + str(data['projectId']), params=data)
        print(self.base_url + str(data['projectId']))
        result = json.dumps(r.json())
        result1 = r.json()
       # result1 = json.dumps(result)
       #  with open("projectinfo_12859.txt",'r+') as wq:
       #      content = wq.read()
        print(type(result))
       #  print(type(r))
        print(result1)
        #self.assertEqual(result,content)
        # result['data']['project'].pop('allowInvestAt')
        # result['data']['project'].pop('bidCompletedTime')
        # result['data']['project'].pop('intdate')
       # print(result)
        #print(result['data']['project']['projectName'])









    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()