import unittest, requests, os, sys
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function")
sys.path.append(dir + "/data_configuration")
from get_data import GetData
from get_token import get_chekToken, get_auth_token, get_stampToken, get_loginpass, SmsCode


class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.url = GetData.url
        self.base_url = self.url + "/user/register"

    @parameterized.expand([("test_register_success", "12345678910", "123456", "Register", "000000", "appstore", "APP")])
    def test_register(self, name, mobile, password, smsType, mobileCode, channel, source):
        accessKey_url = self.url + "/token/accessToken"
        response = requests.request('post', url=accessKey_url, data={'userName': mobile})
        access_key = response.json()['data']
        # print(access_key)
        loginpass_encrypt = get_loginpass(access_key, password)
        #获取手机验证码
        SmsCode(sessionKey="123", mobilephone=mobile, smsType=smsType)
        test_data1 = {'mobile': mobile, 'mobileCode': mobileCode, 'loginPass': loginpass_encrypt.decode(),
                      'channel': channel, 'recommendCode': '', 'adid': '', 'source': source}
        checkToken = get_chekToken(**test_data1)
        test_data = {'mobile': mobile, 'mobileCode': mobileCode, 'loginPass': loginpass_encrypt,
                     'channel': channel, 'recommendCode': '', 'adid': '', 'checkToken': checkToken, 'source': source}
        r = requests.request('post', url=self.base_url, data=test_data)
        result = r.json()
        print(result)
        #self.assertEqual(result['data']['mobile'], mobile)


if __name__ == '__main__':
    unittest.main()




