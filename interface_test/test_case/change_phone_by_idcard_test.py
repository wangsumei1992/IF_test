import unittest, requests, os, sys
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function/")
sys.path.append(dir + "/data_configuration/")
from get_token import get_stampToken, get_chekToken, get_loginpass, get_auth_token
from get_data import GetData


class ChangePhoneIdCardTest(unittest.TestCase):
    """手机号修改-使用身份证解绑"""
    url = GetData.url

    def setUp(self):
        self.base_url = self.url + "/user/unbindmobilebyidcard"

    @parameterized.expand([('success', '34233219730605225X','堂泽','解绑手机成功'),
                           ('idcard_null','','堂泽','身份证号不符'),
                           ('realname_null','34233219730605225X','','姓名不符'),
                           ('all_null', '', '','身份证号不符'),
                           ('name_idcard_notmatch','342133219730605225X','堂泽','身份证号不符')
                           ])
    def testchangephone(self, name, idcard, realname,msg):
        """带token的请求"""
        self.authToken = get_auth_token("c2446993", "15458524695")
        data = {'idCard':idcard, 'realName':realname,'authToken':self.authToken}
        response = requests.request('post',url=self.base_url,data=data)
        self.result = response.json()

        self.assertEqual(self.result['msg'],msg)
    def test_token_null(self):
        """token与要解绑的用户信息不符"""
        authtoken = get_auth_token('15458524705','15458524705')
        data = {'idCard': '342133219730605225X', 'realName': '堂泽', 'authToken': authtoken}
        response = requests.request('post', url=self.base_url, data=data)
        self.result = response.json()
        self.assertEqual(self.result['msg'], '身份证号不符')
    def tearDown(self):
        print(self.result)
if __name__ == '__main__':
    unittest.main()


