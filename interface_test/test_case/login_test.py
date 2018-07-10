import unittest, requests, os, sys
from parameterized import parameterized

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function/")
sys.path.append(dir + "/data_configuration/")
from get_token import get_stampToken, get_chekToken, get_loginpass
from get_data import GetData


class LoginTest(unittest.TestCase):
    url = GetData.url
    def setUp(self):
        self.base_url = self.url + "/user/login"
    @parameterized.expand([( "login_success", "", "", "15458524695", "123", "WEB", "c2446993", "1", "1", "登录成功"),
                           # ("login_username_null", "", "", "15458524695", "123", "WEB", "", "1","0","用户名错误"),
                           # ("login_username_error", "", "", "15458524695", "123", "WEB", "error154585", "1", "0","用户名或密码不正确"),
                           # ("login_pass_null", "", "", "", "123", "WEB", "15458524695", "1", "0", "用户名或密码不正确"),
                           # ("login_pass_error", "", "", "error123", "123", "WEB", "15458524695", "1", "0", "用户名或密码不正确"),
                           # ("login_vail_code_error", "", "", "15458524695", "123", "WEB", "15458524695", "12", "0", "验证码错误"),
                           # ("all_null", "", "", "", "123", "WEB", "", "", "0", "验证码错误"),
                           # ("all_wrong", "", "", "error123", "123", "WEB", "error_username", "12", "0", "验证码错误"),
                           ])
    def test_login(self, name, checkToken, device_id, loginPass,sessionKey, source, userName, validateCode, code, msg):
        """登录接口测试"""
        sessionkey_url = self.url + "/createValidateCode"
        accessKey_url = self.url + "/token/accessToken"
        # 获取图形验证码
        requests.request('post', url=sessionkey_url, data={'sessionKey': sessionKey})
        # 获取accessKey
        response = requests.request('post', url=accessKey_url, data={'userName':userName})
        print(response.json())
        accessKey = response.json()['data']
        loginpass_encrypt = get_loginpass(accessKey,loginPass)
        testdata = {'checkToken':checkToken, 'device_id':device_id, 'loginPass':loginpass_encrypt,
                    'sessionKey':sessionKey, 'source':source, 'userName':userName, 'validateCode':validateCode}
        r = requests.request('post', url=self.base_url, data=testdata)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], int(code))
        self.assertIn(msg,result['msg'])

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
