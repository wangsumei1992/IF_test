import unittest, requests, os, sys
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function")
sys.path.append(dir + "/data_configuration")
from get_data import GetData
from get_token import get_auth_token, get_chekToken, get_stampToken

class ChangePasswordTest(unittest.TestCase):

    def setUp(self):
        url = GetData.url
        self.base_url = url + "/user/savePassword"

    def test_changepass(self):
        #stampToken = str(get_stampToken())
        auth_token = get_auth_token(userName='15558524696', loginPass='15558524696')
        test_data = {'authToken': auth_token, 'oldPassword': '123456', 'newPassword': '111111', 'source': 'APP'}
        r = requests.request('post', url=self.base_url, data=test_data)
        #r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        print(result)

if __name__ == '__main__':
    unittest.main()