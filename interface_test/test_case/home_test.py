import unittest
import os, sys
import requests
from parameterized import parameterized
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/data_configuration")
from get_data import GetData

class HomeTest(unittest.TestCase):

    def setUp(self):
        url = GetData.url
        self.base_url = url + "/"

    def test_houseProject(self):
        """优选专区推荐房易融标的"""
        test_data = {}
        r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        #print(result)
        #print(result['data']['houseProject'])
        self.assertEqual(result['code'], 1)
        self.assertEqual(result['msg'], 'web首页请求数据成功')
        self.assertEqual(result['data']['houseProject']['projectName'], '房易融推荐标')

    def test_homeProject(self):
        """优选专区推荐信标"""
        test_data = {}
        r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        #print(result['data']['homeProject'])
        self.assertEqual(result['code'], 1)
        self.assertEqual(result['data']['homeProject']['projectName'], '信易融标的')

    def test_noticeList(self):
        """新闻资讯"""
        test_data = {}
        r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        #print(result['data']['noticeList'][0])
        self.assertEqual(result['data']['noticeList'][0]['caller'], 'Web')
        self.assertEqual(result['data']['noticeList'][0]['cmsTitle'], '新闻大事件暴走大事件')

    def test_reportList(self):
        """公司动态"""
        test_data = {}
        r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        self.assertEqual(result['data']['reportList'][0]['caller'], 'Web')
        self.assertEqual(result['data']['reportList'][0]['cmsTitle'], '上半年业绩重大突破')

    def test_newNoticeList(self):
        """公告通知"""
        test_data = {}
        r = requests.request('get', url=self.base_url, params=test_data)
        result = r.json()
        #print(result['data']['newNoticeList'])
        self.assertEqual(result['data']['newNoticeList'][0]['caller'], 'Web')
        self.assertEqual(result['data']['newNoticeList'][0]['cmsTitle'], '小幸运')

    # def test_bannerList(self):
    #     """首页banner"""
    #     test_data = {}
    #     r = requests.request('get', url=self.base_url, params=test_data)
    #     result = r.json()
    #     print(result)
    #     print(result['data']['bannerList'][0]['description'], '感恩信任 亿起出发')

if __name__ == '__main__':
    unittest.main()

