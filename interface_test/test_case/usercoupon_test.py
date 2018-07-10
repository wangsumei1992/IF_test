import unittest, requests, os, sys
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function/")
sys.path.append(dir + "/data_configuration/")
from get_token import get_stampToken, get_chekToken, get_loginpass, get_auth_token
from get_data import GetData


class UserCoupon(unittest.TestCase):
    """我的奖励，用户红包、加息券、兑现券展示测试"""
    url = GetData.url
    def setUp(self):
        self.base_url = self.url + "/coupon"

    @parameterized.expand([('hongbao_jiaxi','coupon','查询用户红包成功',1),
                           ('hongbao_duixian','couponcash','查询用户红包成功',2),
                           ('duixian', 'cash','查询用户红包成功',1)
                           ])
    def test_APP_withtoken(self,name,couponType,msg,nums):
        """移动端展示测试"""
        authtoken = get_auth_token("c2446993", "15458524695")
        stampToken = get_stampToken()
        data = {'authToken': authtoken, 'stampToken': str(stampToken),'page':'1','source':'APP','couponType':couponType}
        chcketoken = get_chekToken(**data)
        data_params = {'authToken': authtoken, 'stampToken': stampToken,'page':'1','source':'APP','couponType':couponType,
                       'checkToken':chcketoken}
        response = requests.request('get', url=self.base_url, params=data_params)
        self.result = response.json()
        self.assertEqual(self.result['msg'],msg)
        self.assertEqual(len(self.result['item']['list']),nums)

    @parameterized.expand([('hongbao_jiaxi', 'coupon', '登录已失效，请重新登录。'),
                           ('hongbao_duixian', 'couponcash', '登录已失效，请重新登录。'),
                           ('duixian', 'cash', '登录已失效，请重新登录。')
                           ])
    def test_APP_null_token(self,name,couponType,msg):
        """移动端展示未登录"""
        stampToken = get_stampToken()
        data = {'stampToken': str(stampToken), 'page': '', 'source': 'APP',
                'couponType': couponType}
        chcketoken = get_chekToken(**data)
        data_params = {'stampToken': stampToken, 'page': '', 'source': 'APP',
                       'couponType': couponType,
                       'checkToken': chcketoken}
        response = requests.request('get', url=self.base_url, params=data_params)
        self.result = response.json()
        self.assertEqual(self.result['msg'], msg)

    @parameterized.expand([('first_page','1','查询用户红包成功'),
                           ('second_page', '2','查询用户红包失败')
                           ])
    def test_APP_paging(self,name,page,msg):
        """测试移动端分页功能"""
        authtoken = get_auth_token("c2446993", "15458524695")
        stampToken = get_stampToken()
        data = {'authToken': authtoken, 'stampToken': str(stampToken), 'page': page, 'source': 'APP',
                'couponType': 'coupon'}
        chcketoken = get_chekToken(**data)
        data_params = {'authToken': authtoken, 'stampToken': stampToken, 'page': page, 'source': 'APP',
                       'couponType': 'coupon',
                       'checkToken': chcketoken}
        response = requests.request('get', url=self.base_url, params=data_params)
        self.result = response.json()
        self.assertEqual(self.result['msg'],msg)

    @parameterized.expand([('hongbao_jiaxi', 'coupon','','', '查询用户红包成功', 1),
                           ('hongbao_duixian', 'couponcash','','', '查询用户红包成功', 2),
                           ('duixian', 'cash','','','查询用户红包成功', 1)
                           ])
    def test_WEB_withtoken(self, name, couponType,istatus,couponFlag, msg, nums):
        """PC端展示测试"""
        authtoken = get_auth_token("c2446993", "15458524695")
        stampToken = get_stampToken()
        data = {'authToken': authtoken, 'stampToken': str(stampToken), 'page': '1', 'source': 'WEB',
                'couponType': couponType,'istatus':istatus,'couponFlag':couponFlag}
        chcketoken = get_chekToken(**data)
        data_params = {'authToken': authtoken, 'stampToken': stampToken, 'page': '1', 'source': 'WEB',
                       'couponType': couponType,'istatus':istatus,'couponFlag':couponFlag,'checkToken': chcketoken}
        response = requests.request('get', url=self.base_url, params=data_params)
        self.result = response.json()
        self.assertEqual(self.result['msg'], msg)
        self.assertEqual(len(self.result['item']['list']), nums)

    @parameterized.expand([('first_page', '1', '查询用户红包成功'),
                           ('second_page', '2', '查询用户红包失败')
                           ])
    def test_WEB_paging(self, name, page, msg):
        """测试PC分页功能"""
        authtoken = get_auth_token("c2446993", "15458524695")
        stampToken = get_stampToken()
        data = {'authToken': authtoken, 'stampToken': str(stampToken), 'page': page, 'source': 'WEB',
                'couponType': 'coupon'}
        chcketoken = get_chekToken(**data)
        data_params = {'authToken': authtoken, 'stampToken': stampToken, 'page': page, 'source': 'WEB',
                       'couponType': 'coupon',
                       'checkToken': chcketoken}
        response = requests.request('get', url=self.base_url, params=data_params)
        self.result = response.json()
        self.assertEqual(self.result['msg'], msg)

    @parameterized.expand([('hongbao_jiaxi', 'coupon', '登录已失效，请重新登录。'),
                           ('hongbao_duixian', 'couponcash', '登录已失效，请重新登录。'),
                           ('duixian', 'cash', '登录已失效，请重新登录。')
                           ])
    def test_WEB_null_token(self, name, couponType, msg):
        """PC端展示未登录"""
        stampToken = get_stampToken()
        data = {'stampToken': str(stampToken), 'page': '', 'source': 'WEB',
                'couponType': couponType}
        chcketoken = get_chekToken(**data)
        data_params = {'stampToken': stampToken, 'page': '', 'source': 'WEB',
                       'couponType': couponType,
                       'checkToken': chcketoken}
        response = requests.request('get', url=self.base_url, params=data_params)
        self.result = response.json()
        self.assertEqual(self.result['msg'], msg)

    def test_WEB_couponFlag(self):
        """我的账户账户总览中红包数,返回参数都一样"""
        authtoken = get_auth_token("c2446993", "15458524695")
        stampToken = get_stampToken()
        data = {'authToken': authtoken, 'stampToken': str(stampToken), 'page': '1', 'source': 'WEB',
                'couponType': 'couponcash', 'istatus': 'available', 'couponFlag': ''}
        chcketoken = get_chekToken(**data)
        data_params = {'authToken': authtoken, 'stampToken': stampToken, 'page': '1', 'source': 'WEB',
                       'couponType': 'couponcash','istatus': 'available',
                       'couponFlag': '','checkToken': chcketoken}
        response = requests.request('get', url=self.base_url, params=data_params)
        self.result = response.json()
        self.assertEqual(self.result['msg'],'查询用户红包成功')
        self.assertEqual(len(self.result['item']['list']),2)

    @parameterized.expand([('weiyong', 'available', '查询用户红包成功', 2),
                           ('yiyong', 'used', '查询用户红包成功', 2),
                           ('yisuoding', 'locked', '查询用户红包成功', 2),
                           ])
    def test_WEB_istatus(self, name, istatus,msg, nums):
        """PC端红包状态测试"""
        authtoken = get_auth_token("c2446993", "15458524695")
        stampToken = get_stampToken()
        data = {'authToken': authtoken, 'stampToken': str(stampToken), 'page': '1', 'source': 'WEB',
                'couponType': 'couponcash', 'istatus': istatus, }
        chcketoken = get_chekToken(**data)
        data_params = {'authToken': authtoken, 'stampToken': stampToken, 'page': '1', 'source': 'WEB',
                       'couponType': 'couponcash', 'istatus': istatus, 'checkToken': chcketoken}
        response = requests.request('get', url=self.base_url, params=data_params)
        self.result = response.json()
        self.assertEqual(self.result['msg'], msg)
        self.assertEqual(len(self.result['item']['list']), nums)

    def tearDown(self):
        print(self.result)
if __name__ == '__main__':
    unittest.main()