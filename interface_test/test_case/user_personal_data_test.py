import unittest, requests, os, sys
from parameterized import parameterized

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function/")
sys.path.append(dir + "/data_configuration/")
from get_token import get_stampToken, get_chekToken, get_auth_token
from get_data import GetData


class UserPersonDataTest(unittest.TestCase):
    url = GetData.url
    def setUp(self):
        self.base_url = self.url + "/user/info"

    @parameterized.expand([('test_OpenSumaPay_success1', '13658524690', '15811507614', False, True, True),
                           ('test_OpenSumaPay_borrowPermission', '14458526670', '14458526670', True, True, True),
                           ('test_OpenSumaPay_isnot', '15458524698', '15458524698', False, False, False),
                           ('test_OpenSumaPay_isNotPayPassword', '13658524691', '15811507614', False, True, False)])
    def test_OpenSumaPay(self, name, username, password, message1, message2, message3):
        """出借人/借款人开户、设置交易密码"""
        auth_token = get_auth_token(username, password)
        r = requests.request('get', url=self.base_url, params={"authToken": auth_token})
        #data={'borrowPermission': borrowPermission, 'openAcctId':openAcctId}
        result = r.json()
        print(result)
        # print(result['data']['isOpenSumaPay'])
        # print(result['data']['isPayPassword'])
        self.assertIs(result['data']['borrowPermission'], message1)
        self.assertIs(result['data']['isOpenSumaPay'], message2)
        self.assertIs(result['data']['isPayPassword'], message3)
        #print(r.json()['data'])
        # print(type(r.json()['data']))
        # self.assertEqual(data, r.json()['data'])

if __name__ == '__main__':
    unittest.main()




