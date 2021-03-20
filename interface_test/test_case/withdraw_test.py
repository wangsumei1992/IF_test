import unittest, requests, os, sys, json
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function/")
sys.path.append(dir + "/data_configuration/")
from get_token import get_stampToken, get_chekToken, get_loginpass, get_auth_token
from get_data import GetData


class WithDrawTest(unittest.TestCase):
    """提现测试"""
    url = GetData.url

    def setUp(self):
        self.base_url = self.url + "/withdrawcash/startWithdraws"

    def qtest_large(self):
        """大额提现"""
        authtoken = get_auth_token()
        stampToken = get_stampToken()
        data = {'authToken': authtoken, 'stampToken': str(stampToken),'bankCnaps':'102138111868',
                'source': 'APP','amount': '1000','routFlag':'Y'}
        data_start ={'authToken': authtoken, 'stampToken': str(stampToken)}
        checktoken = get_chekToken(**data)
        checktoken1 = get_chekToken(**data_start)
        data_params = {'authToken': authtoken, 'stampToken': str(stampToken),'bankCnaps':'102138111868',
                       'source': 'APP','amount': '1000','routFlag':'Y','checkToken':checktoken}
        # 提现初始化
        data_start_params = {'authToken': authtoken, 'stampToken': str(stampToken),'checkToken':checktoken1}
        requests.request('get',url=self.url+"/withdrawcash",params=data_start_params)
        response = requests.request('post',url=self.base_url,data=data_params)
        self.result = response.json()

    def test_realtime(self):
        """实时提现"""
        authtoken = get_auth_token()
        stampToken = get_stampToken()
        data = {'authToken': authtoken, 'stampToken': str(stampToken),
                'source': 'APP','amount': '1000','routFlag':'N'}
        data_start = {'authToken': authtoken, 'stampToken': str(stampToken)}
        checktoken1 = get_chekToken(**data_start)
        checktoken = get_chekToken(**data)
        data_params = {'authToken': authtoken, 'stampToken': str(stampToken),
                       'source': 'APP','amount': '1000','routFlag':'N','checkToken':checktoken}
        # 提现初始化
        data_start_params = {'authToken': authtoken, 'stampToken': str(stampToken), 'checkToken': checktoken1}
        q=requests.request('get', url=self.url + "/withdrawcash", params=data_start_params)
        print(q.json())
        response = requests.request('post',url=self.base_url,data=data_params)
        self.result = response.json()
    def tearDown(self):
        print(self.result)

if __name__ == '__main__':
    unittest.main()