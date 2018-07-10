import unittest,requests, os, sys
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function/")
sys.path.append(dir + "/data_configuration/")
from get_token import get_stampToken, get_chekToken, get_auth_token
from get_data import GetData


class ProjectListTest(unittest.TestCase):
    def setUp(self):
        url = GetData.url
        self.base_url = url + "/project/list0"

    @parameterized.expand([('web_projectCategory_qi', 'WEB', '4', '1', '2', '2', '', '','企易融','企易融'),
                           # ('web_projectCategory_che', 'WEB', '1', '1', '2', '', '', '','车易融','车易融'),
                           # ('web_projectCategory_xin', 'WEB', '2', '1', '2', '', '', '','信易融','信易融'),
                           # ('web_projectCategory_fang', 'WEB', '3', '1', '2', '', '', '','房易融','房易融'),
                           # ('web_projectCategory_all', 'WEB', '', '1', '8', '', '', '', '车易融','车易融'),
                           # ('web_page', 'WEB', '', '1', '2', '', '', '', '车易融', '信易融'),
                           # ('web_page', 'WEB', '', '2', '2', '', '', '', '信易融', '信易融'),
                           ])

    def test_projectCategory(self, name, source, projectCategory, page, pageSize,
                      projectStatus, searchTime, projectNewType, message1,message2):
        """WEB项目类型查询测试"""
        stampToken = str(get_stampToken())
        auth_token = get_auth_token("c2446993", "15458524695")
        test_data1 = {'stampToken': stampToken,'source': source,
                     'page': page, 'pageSize': pageSize, 'searchTime': searchTime,
                     'projectNewType': projectNewType, 'projectCategory': projectCategory,'authToken':auth_token}
        checkToken = get_chekToken(**test_data1)
        test_data = {'stampToken': stampToken, 'checkToken':checkToken, 'source': source,
                     'page': page, 'pageSize': pageSize, 'searchTime': searchTime,
                     'projectNewType': projectNewType, 'projectCategory': projectCategory,
                     'projectStatus':projectStatus}

        r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], 1)
        self.assertEqual(result['item']['list'][0]['projectCategory'], message1)
        self.assertEqual(result['item']['list'][-1]['projectCategory'], message2)

    # @parameterized.expand([('web_pagesize_8', 'WEB', '4', '1', '8', '', '', '','8'),
    #                        ('web_pagesize_4', 'WEB', '4', '1', '4', '', '', '', '4'),
    #                        ('APP_pagesize_8', 'APP', '4', '1', '8', '', '', '', '8'),
    #                        ('APP_pagesize_4', 'APP', '4', '1', '4', '', '', '', '4'),])
    # def test_pagesize(self, name, source, projectCategory, page, pageSize,
    #                   projectStatus, searchTime, projectNewType, num):
    #     """WEB、APP每页条数测试"""
    #     stampToken = str(get_stampToken())
    #     test_data1 = {'stampToken': stampToken, 'source': source,
    #                   'page': page, 'pageSize': pageSize, 'searchTime': searchTime,
    #                   'projectNewType': projectNewType, 'projectCategory': projectCategory}
    #     checkToken = get_chekToken(**test_data1)
    #     test_data = {'stampToken': stampToken, 'checkToken': checkToken, 'source': source,
    #                  'page': page, 'pageSize': pageSize, 'searchTime': searchTime,
    #                  'projectNewType': projectNewType, 'projectCategory': projectCategory,
    #                  'projectStatus': projectStatus}
    #
    #     r = requests.request('get', url=self.base_url, params=test_data)
    #     result = r.json()
    #     self.assertEqual(len(result['item']['list']),int(num))
    #
    #
    # @parameterized.expand([('web_inprocess', 'WEB', '', '1', '8', '1', '', '', 'inProcess', 'inProcess', 'status'),
    #                        ('web_finish', 'WEB', '', '1', '8', '2', '', '', 'finish','finish','status'),
    #                        ('web_clear', 'WEB', '', '1', '8', '3', '', '', 'clear', 'clear', 'status'),
    #                        ('web_status_all', 'WEB', '', '1', '8', '0', '', '', 'inProcess', 'clear', 'status'),
    #                        ('web_time_all', 'WEB', '', '1', '8', '0', '0', '', '0.50', '24.0', 'financingMaturity'),
    #                        ('web_time_0-1', 'WEB', '', '1', '8', '0', '1', '', '0.50', '0.50', 'financingMaturity'),
    #                        ('web_time_1-3', 'WEB', '', '1', '8', '0', '2', '', '1.0', '1.0', 'financingMaturity'),
    #                        ('web_time_3-6', 'WEB', '', '1', '8', '0', '3', '', '4.0', '3.0', 'financingMaturity'),
    #                        ('web_time_6-12', 'WEB', '', '1', '8', '0', '4', '', '6.0', '7.0', 'financingMaturity'),
    #                        ('web_time_12-24', 'WEB', '', '1', '8', '0', '4', '', '12.0', '24.0', 'financingMaturity'),
    #                       #  ('web_group_search1', 'WEB', '2', '1', '8', '1', '4', '', '信1', '信2', 'projectName'),
    #                       # ('web_group_search2', 'WEB', '1', '1', '8', '3', '3', '', '车1', '车1', 'projectName'),
    #                       #  ('web_group_search3', 'WEB', '4', '1', '8', '2', '2', '', '企2', '企2', 'projectName'),
    #                        ])
    # def test_status_and_searchTime(self, name, source, projectCategory, page, pageSize,
    #                           projectStatus, searchTime, projectNewType, first_value, last_value, key):
    #     """WEB项目状态与借款期限测试"""
    #     stampToken = str(get_stampToken())
    #     test_data1 = {'stampToken': stampToken, 'source': source,
    #                   'page': page, 'pageSize': pageSize, 'searchTime': searchTime,
    #                   'projectNewType': projectNewType, 'projectCategory': projectCategory,
    #                   'projectStatus': projectStatus}
    #     checkToken = get_chekToken(**test_data1)
    #     test_data = {'stampToken': stampToken, 'checkToken': checkToken, 'source': source,
    #                  'page': page, 'pageSize': pageSize, 'searchTime': searchTime,
    #                  'projectNewType': projectNewType, 'projectCategory': projectCategory,
    #                  'projectStatus': projectStatus}
    #
    #     r = requests.request('get', url=self.base_url, params=test_data)
    #     result = r.json()
    #     print(result)
    #     self.assertEqual(result['code'], 1)
    #     self.assertEqual(result['item']['list'][0][key], first_value)
    #     self.assertEqual(result['item']['list'][-1][key], last_value)
    #
    # @parameterized.expand([('web_group_search1', 'WEB', '2', '1', '8', '1', '4', '', '信1', '信2', 'projectName'),
    #                        ('web_group_search2', 'WEB', '1', '1', '8', '3', '3', '', '车1', '车1', 'projectName'),
    #                        ('web_group_search3', 'WEB', '4', '1', '8', '2', '2', '', '企2', '企2', 'projectName'),
    #                        ])
    # def test_group_terms(self, name, source, projectCategory, page, pageSize,
    #                           projectStatus, searchTime, projectNewType,first_value, last_value, key):
    #     """WEB多条件组合查询测试"""
    #     stampToken = str(get_stampToken())
    #     test_data1 = {'stampToken': stampToken, 'source': source,
    #                   'page': page, 'pageSize': pageSize, 'searchTime': searchTime,
    #                   'projectNewType': projectNewType, 'projectCategory': projectCategory,
    #                   'projectStatus': projectStatus}
    #     checkToken = get_chekToken(**test_data1)
    #     test_data = {'stampToken': stampToken, 'checkToken': checkToken, 'source': source,
    #                  'page': page, 'pageSize': pageSize, 'searchTime': searchTime,
    #                  'projectNewType': projectNewType, 'projectCategory': projectCategory,
    #                  'projectStatus': projectStatus}
    #
    #     r = requests.request('get', url=self.base_url, params=test_data)
    #     result = r.json()
    #     print(result)
    #     self.assertEqual(result['code'], 1)
    #     self.assertEqual(result['item']['list'][0][key], first_value)
    #     self.assertEqual(result['item']['list'][-1][key], last_value)



if __name__ == '__main__':
    unittest.main()
