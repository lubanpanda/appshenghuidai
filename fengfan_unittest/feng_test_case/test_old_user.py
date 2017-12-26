import unittest,time
from fengfan_unittest.startAPP import *
from fengfan_unittest.feng_test_method.method import *
import  unittest,requests,HTMLTestRunner
from fengfan_unittest.feng_test_conf.feng_test_env.feng_test_config import *
newuser='13590283182'
class NewuserCode(unittest.TestCase):
    def setUp(self):
        start_App.__init__(self)
        start_App.setUp(self)
        startMethod.loginCode(self,newuser)
    def tearDown(self):
        start_App.tearDown(self)
        startMethod.backLogin(self)


