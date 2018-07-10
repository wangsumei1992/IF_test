import unittest, requests, os, sys
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function")
sys.path.append(dir + "/data_configuration")
from get_data import GetData
from get_token import get_chekToken, get_auth_token, get_stampToken

class CashcouponTest(unittest.TestCase):

    def setUp(self):
        url = GetData.url
        self.base_url = url + "/coupon/usecashcoupon"

    @parameterized.expand([('test_cashcouponNotexist', 'm4927646', '15558524696', '2i80yo4x1v42u7h3', '兑现券兑现失败:兑现券不存在'),
                           ('test_cashcouponUsed', '15458524695', '15458524695', '6q2u46caw84y8m15', '兑现券兑现失败:兑现券已使用'),
                           ('test_cashcouponSuccess', '15458524695', '15458524695', '2i80yo4x1v42u7h3', '兑现券兑现失败')
                           ])
    def test_cashcoupon(self, name, username, loginpass, couponcode, message):
        stampToken = str(get_stampToken())
        authtoken = get_auth_token(userName=username, loginPass=loginpass)
        test_data1 = {'authToken': authtoken, 'stampToken': stampToken, 'couponCode': couponcode}
        check_token = get_chekToken(**test_data1)
        test_data = {'authToken': authtoken, 'stampToken': stampToken, 'checkToken': check_token,
                     'couponCode': couponcode}
        r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        print(result)
        self.assertEqual(result['msg'], message)

if __name__ == '__main__':
    unittest.main()