import unittest, requests, os, sys
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function/")
sys.path.append(dir + "/data_configuration/")
from get_token import get_stampToken, get_chekToken, get_loginpass, get_auth_token
from get_data import GetData


class ReCharge(unittest.TestCase):
    """测试充值数据初始化"""
    url = GetData.url

    def setUp(self):
        self.base_url = self.url + "/recharge"

    def test1(self):
        authtoken = get_auth_token()
        stampToken = get_stampToken()
        data = {'authToken': authtoken, 'stampToken': str(stampToken), 'source': 'APP','seqNo':''}
        checktoken = get_chekToken(**data)
        data_params = {'authToken': authtoken, 'stampToken': str(stampToken), 'source': 'APP','checkToken':checktoken,
                       'seqNo': ''}
        response = requests.request('get', url=self.base_url, params=data_params)
        self.result = response.json()

    def tearDown(self):
        print(self.result)

if __name__ == '__main__':
    unittest.main()
