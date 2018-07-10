import unittest, requests, os, sys
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function/")
sys.path.append(dir + "/data_configuration/")
from get_token import get_stampToken, get_chekToken, get_loginpass, get_auth_token
from get_data import GetData


class ReferrerUserTest(unittest.TestCase):
    """我的账户-推荐好友"""
    url = GetData.url

    def setUp(self):
        self.base_url = self.url + "/recommend"

    @parameterized.expand([('first_page','1'),
                           ('other_page','3')
                           ])
    def test_web(self,name,page):
        """推荐好友查询web"""
        authtoken = get_auth_token()
        stampToken = get_stampToken()
        data = {'authToken': authtoken, 'stampToken': str(stampToken), 'page': page, 'source': 'WEB'}
        chcketoken = get_chekToken(**data)
        data_params = {'authToken': authtoken, 'stampToken': str(stampToken),'checkToken':chcketoken,
                       'page': page, 'source': 'WEB'}
        response = requests.request('get', url=self.base_url, params=data_params)
        self.result = response.json()
        self.assertEqual(self.result['msg'],'推荐好友请求成功')

    @parameterized.expand([('first_page', '1'),
                           ('other_page', '50')
                           ])
    def test_APP(self, name, page):
        """推荐好友查询APP"""
        authtoken = get_auth_token()
        stampToken = get_stampToken()
        data = {'authToken': authtoken, 'stampToken': str(stampToken), 'page': page, 'source': 'APP'}
        chcketoken = get_chekToken(**data)
        data_params = {'authToken': authtoken, 'stampToken': str(stampToken), 'checkToken': chcketoken,
                       'page': page, 'source': 'APP'}
        response = requests.request('get', url=self.base_url, params=data_params)
        self.result = response.json()
        self.assertEqual(self.result['msg'], '推荐好友请求成功')

    def tearDown(self):
        print(self.result)

if __name__ == '__main__':
    unittest.main()
