import unittest, requests, os, sys, json
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function/")
sys.path.append(dir + "/data_configuration/")
from get_token import get_stampToken, get_chekToken, get_loginpass, get_auth_token
from get_data import GetData


class QuickRechargeTest(unittest.TestCase):
    """快捷充值支付密码验证测试"""
    url = GetData.url

    def setUp(self):
        self.base_url = self.url + "/recharge/quickRechargeVerifyPwd"

    def test(self):
        authtoken = get_auth_token()
        stampToken = get_stampToken()
        data = {'authToken': authtoken, 'stampToken': str(stampToken),'source': 'APP','amount': '100'}
        checkToken = get_chekToken(**data)
        data_params = {'authToken': authtoken, 'stampToken': str(stampToken),'source': 'APP','amount': '100',
                       'checkToken':checkToken}
        response = requests.request('post', url=self.base_url, data=data_params)
        self.result = response.json()

    def tearDown(self):
        print(self.result)

if __name__ == '__main__':
    unittest.main()
