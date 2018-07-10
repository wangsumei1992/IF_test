import unittest, requests, os, sys
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function")
sys.path.append(dir + "/data_configuration")
from get_data import GetData
from get_token import get_chekToken, get_auth_token, get_stampToken


class MessageTest(unittest.TestCase):

    def setUp(self):
        url = GetData.url
        self.base_url = url + "/msg/msg"

    @parameterized.expand([('test_Appmessage', '15458524695', '15458524695', '', '', 'APP'),
                          ])
    def test_Appmessage(self, name, username, loginpass, page, isRead, source):
        stampToken = str(get_stampToken())
        authToken = get_auth_token(userName=username, loginPass=loginpass)
        test_data1 = {'stampToken': stampToken, 'authToken': authToken, 'page': page, 'isRead': isRead, 'source': source}
        checkToken = get_chekToken(**test_data1)
        test_data = {'stampToken': stampToken, 'authToken': authToken, 'checkToken': checkToken, 'page': page,
                     'isRead': isRead, 'source': source}
        r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        print(result['data'][0])
        self.assertEqual(result['code'], 1)
        self.assertEqual(result['msg'], '消息中心数据')
        self.assertIn('您已于', result['data'][0]['msgContent'])

if __name__ == '__main__':
    unittest.main()

