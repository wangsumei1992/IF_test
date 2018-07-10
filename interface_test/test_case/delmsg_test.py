import unittest, requests, os, sys
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function")
sys.path.append(dir + "/data_configuration")
from get_data import GetData
from get_token import get_chekToken, get_auth_token, get_stampToken

class DelmsgTest(unittest.TestCase):

    def setUp(self):
        url = GetData.url
        self.base_url = url + "/msg/delMsg"

    @parameterized.expand([('test_delmsg_success', '15458524695', '15458524695', '25295', '删除站内信成功'),
                           ('test_delmsg_notexist', '15458524695', '15458524695', '', '删除站内信成功')
                           ])
    def test_delmsg(self, name, username, loginpass, msgID, message):
        stampToken = str(get_stampToken())
        authToken = get_auth_token(userName=username, loginPass=loginpass)
        test_data1 = {'stampToken': stampToken, 'authToken': authToken, 'msgID': msgID}
        checkToken = get_chekToken(**test_data1)
        test_data = {'stampToken': stampToken, 'authToken': authToken, 'checkToken': checkToken, 'msgID': msgID}
        r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        print(result)
        self.assertEqual(result['msg'], message)

if __name__ == '__main__':
    unittest.main()