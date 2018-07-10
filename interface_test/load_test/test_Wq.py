import unittest
from parameterized import parameterized
import HTMLTestRunner
def add(a,b):
    return a+b


class TestAdd(unittest.TestCase):
    def setUp(self):
        print("start")
    @parameterized.expand([(1,2,3),
                           (2, 2, 4)])
    def test1(self,a,b,c):
        """测试测试"""
        result = add(a,b)
        self.assertEqual(result,c)
    def setUp(self):
        print("end....")

if __name__ == '__main__':
    unittest.main()