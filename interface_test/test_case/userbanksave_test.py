import unittest, requests, os, sys
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function")
sys.path.append(dir + "/data_configuration")
from get_data import GetData
from get_token import get_auth_token, get_chekToken, get_stampToken

class UserBanksave(unittest.TestCase):

    def setUp(self):
        url = GetData.url
        self.base_url = url + "/user/banksave"

    @parameterized.expand([('test_banksave1', '15558524696', '15558524696', '9930040050130141373')])
    def test_banksave(self, name, username, loginpass, sumaPayAccountID):
        auth_token = get_auth_token(userName=username, loginPass=loginpass)
        r = requests.request('post', self.base_url, data={'authToken': auth_token})
        result = r.json()
        print(result)
        self.assertIsNotNone(result['data']['balanceInterest'])
        self.assertIsNotNone(result['data']['balance'])
        self.assertIsNotNone(result['data']['frozenAmount'])
        self.assertEqual(result['data']['sumaPayAccountID'], sumaPayAccountID)
        self.assertEqual(result['msg'], '请求成功')

if __name__ == '__main__':
    unittest.main()

