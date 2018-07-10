import unittest, requests, os, sys
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/my_function")
sys.path.append(dir + "/data_configuration")
from get_data import GetData
from get_token import get_auth_token, get_chekToken

class MyPointsTest(unittest.TestCase):

    def setUp(self):
        url = GetData.url
        self.base_url = url + "/points/pointsList"

    def test_mypoints(self):
        auth_token = get_auth_token('15558524696', '15558524696')
        test_data1 = {'page': '1', 'authToken': auth_token}
        checktoken = get_chekToken(**test_data1)
        test_data = {'page': '1', 'authToken': auth_token, 'checkToken': checktoken}
        r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        print(result)

if __name__ == '__main__':
    unittest.main()
