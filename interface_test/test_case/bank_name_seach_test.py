import unittest, requests, os, sys, json
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function/")
sys.path.append(dir + "/data_configuration/")
from get_token import get_stampToken, get_chekToken, get_loginpass, get_auth_token
from get_data import GetData


class BankNameSeachTest(unittest.TestCase):
    """大额提现查询银行名称测试"""
    url = GetData.url

    def setUp(self):
        self.base_url = self.url + "/withdrawcash/bankinfo"

    def test_bankname(self):
        authtoken = get_auth_token()
        stampToken = get_stampToken()
        data = {'authToken': authtoken, 'stampToken': str(stampToken),"bankName":'宣化'}
        chcketoken = get_chekToken(**data)
        data_params = {'authToken': authtoken, 'stampToken': str(stampToken), 'checkToken': chcketoken,'bankName':'宣化'}
        response = requests.request('get', url=self.base_url, params=data_params)
        self.result = response.json()
        # with open('bank_name.txt', 'w') as wq:
        #     wq.write(json.dumps(self.result))
        with open('bank_name.txt', 'r') as file:
            content = file.read()
        self.assertEqual(self.result,json.loads(content))

    def tearDown(self):
        print(self.result)

if __name__ == '__main__':
    unittest.main()