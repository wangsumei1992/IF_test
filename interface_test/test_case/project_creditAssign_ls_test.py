import unittest
import os, sys
import requests
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function")
sys.path.append(dir + "/data_configuration")
from get_token import get_stampToken, get_chekToken
from get_data import GetData

class ProjectcreditAssignList(unittest.TestCase):
    """债转列表测试"""
    def setUp(self):
        url = GetData.url
        self.base_url = url + "/project/creditAssignList"

    @parameterized.expand([('test_searchTime1', '1', '10', 'WEB', '', '1', '', 1.0),
                           ('test_searchTime2', '1', '10', 'WEB', '', '2', '', 2.0),
                           ('test_searchTime3', '1', '10', 'WEB', '', '3', '', 5.0),
                           ('test_searchTime4', '1', '10', 'WEB', '', '4', '', 11.0),
                           ('test_searchTime5', '1', '10', 'WEB', '', '5', '', 23.0),
                           ])
    def test_searchTime(self, name, page, pageSize, source, nextPlanPay, searchTime, interestRate, message):
        """WEB债转标的剩余期限"""
        stampToken = str(get_stampToken())
        test_data1 = {'stampToken': stampToken, 'page': page, 'pageSize': pageSize, 'source': source,
                      'nextPlanPay': nextPlanPay, 'searchTime': searchTime, 'interestRate': interestRate}
        checkToken = get_chekToken(**test_data1)
        test_data = {'stampToken': stampToken, 'checkToken': checkToken, 'page': page, 'pageSize': pageSize,
                     'source': source, 'nextPlanPay': nextPlanPay, 'searchTime': searchTime,
                     'interestRate': interestRate}
        r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        print(result)
        print(result['item']['list'][0]['surplusFinancingMaturity'])
        self.assertEqual(result['code'], 1)
        self.assertEqual(result['msg'], '查询债权转让列表成功')
        self.assertEqual(result['item']['list'][0]['surplusFinancingMaturity'], message)

    @parameterized.expand([('test_interestRate1', '1', '10', 'WEB', '', '', '1', '7.5%'),
                           ('test_interestRate2', '1', '10', 'WEB', '', '', '2', '9.5%'),
                           ('test_interestRate3', '1', '10', 'WEB', '', '', '3', '11%'),
                           ('test_interestRate4', '1', '10', 'WEB', '', '', '4', '11.5%'),
                           ('test_interestRate5', '1', '10', 'WEB', '', '', '5', '12.5%'),
                           ])
    def test_interestRate(self, name, page, pageSize, source, nextPlanPay, searchTime, interestRate, message):
        """年化利率查询"""
        stampToken = str(get_stampToken())
        test_data1 = {'stampToken': stampToken, 'page': page, 'pageSize': pageSize, 'source': source,
                      'nextPlanPay': nextPlanPay, 'searchTime': searchTime, 'interestRate': interestRate}
        checkToken = get_chekToken(**test_data1)
        test_data = {'stampToken': stampToken, 'checkToken': checkToken, 'page': page, 'pageSize': pageSize,
                     'source': source, 'nextPlanPay': nextPlanPay, 'searchTime': searchTime,
                     'interestRate': interestRate}
        r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], 1)
        self.assertEqual(result['item']['list'][0]['displayInterestRate'], message)

    @parameterized.expand([('test_nextPlanPay1', '1', '10', 'WEB', '1', '', '', '列表查询标的测试02'),
                           ('test_nextPlanPay2', '1', '10', 'WEB', '2', '', '', '信用债转标的测试01'),
                           ])
    def test_nextPlanPay(self, name, page, pageSize, source, nextPlanPay, searchTime, interestRate, message):
        """WEB距离下次还款"""
        stampToken = str(get_stampToken())
        test_data1 = {'stampToken': stampToken, 'page': page, 'pageSize': pageSize, 'source': source,
                      'nextPlanPay': nextPlanPay, 'searchTime': searchTime, 'interestRate': interestRate}
        checkToken = get_chekToken(**test_data1)
        test_data = {'stampToken': stampToken, 'checkToken': checkToken, 'page': page, 'pageSize': pageSize,
                     'source': source, 'nextPlanPay': nextPlanPay, 'searchTime': searchTime,
                     'interestRate': interestRate}
        r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], 1)
        self.assertEqual(result['item']['list'][0]['projectName'], message)

    @parameterized.expand([('test_interquery1', '1', '10', 'WEB', '1', '4', '4', '列表查询标的测试02'),
                           ])
    def test_interquery(self, name, page, pageSize, source, nextPlanPay, searchTime, interestRate, message):
        """WEB筛选条件综合查询"""
        stampToken = str(get_stampToken())
        test_data1 = {'stampToken': stampToken, 'page': page, 'pageSize': pageSize, 'source': source,
                      'nextPlanPay': nextPlanPay, 'searchTime': searchTime, 'interestRate': interestRate}
        checkToken = get_chekToken(**test_data1)
        test_data = {'stampToken': stampToken, 'checkToken': checkToken, 'page': page, 'pageSize': pageSize,
                     'source': source, 'nextPlanPay': nextPlanPay, 'searchTime': searchTime,
                     'interestRate': interestRate}
        r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], 1)
        self.assertEqual(result['item']['list'][0]['projectName'], message)

if __name__ == "__main__":
    unittest.main()


