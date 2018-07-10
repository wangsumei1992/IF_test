import unittest, requests, os, sys
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function")
sys.path.append(dir + "/data_configuration")
from get_data import GetData
from get_token import get_stampToken, get_chekToken, get_auth_token

class AppUserTest(unittest.TestCase):

    def setUp(self):
        url = GetData.url
        self.base_url = url + "/user/appuser"

    @parameterized.expand([('test_Appuser1_lenderfull', '15558524696', '15558524696', 'true', 'true'),
                           ('test_Appuser1_notOpensumapy', '15458524698', '15458524698', 'false', 'false'),
                           ('test_Appuser1_NotPayPass', '13658524691', '15811507614', 'true', 'false'),
                           ])
    def test_Appuser(self, name, username, password, message1, message2):
        """app我的账户"""
        stampToken = str(get_stampToken())
        auth_token = get_auth_token(username, password)
        test_data1 = {'stampToken': stampToken, 'authToken': auth_token}
        checkToken = get_chekToken(**test_data1)
        test_data = {'stampToken': stampToken, 'authToken': auth_token, 'checkToken': checkToken}
        r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], 1)
        self.assertEqual(result['msg'], '查询账户总览成功')
        self.assertEqual(result['data']['isOpenSumaPay'], message1)
        self.assertEqual(result['data']['isPayPass'], message2)


if __name__ == '__main__':
    unittest.main()