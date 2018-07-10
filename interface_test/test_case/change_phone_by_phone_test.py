import unittest, requests, os, sys
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function/")
sys.path.append(dir + "/data_configuration/")
from get_token import get_stampToken, get_chekToken, get_loginpass, get_auth_token
from get_data import GetData


class ChangePhoneTest(unittest.TestCase):
    """手机号修改-使用手机验证码解绑"""
    url = GetData.url

    def setUp(self):
        self.base_url = self.url + "/user/unbindmobilebyold"
        self.authToken = get_auth_token("c2446993", "15458524695")


    def test1(self):
        data = {'mobileCode':'000000','authToken':self.authToken}
        response = requests.request('post',url=self.base_url, data=data)
        self.result = response.json()
        #print(result)

    def tearDown(self):
        print(self.result)

if __name__ == '__main__':
    unittest.main()