#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  84305510@qq.com
import unittest

import time

from SHD_automation.device_info.device import *
from SHD_automation.panda_methods.my_methods import My_method, Huadong


class test_Login(unittest.TestCase,object):
	def setUp(self):
		star_app.__init__(self)
		star_app.setup(self)
	def tearDown(self):
		star_app.tearDown(self)

	def test_01_login(self):

		My_method.loginCode(self,15201525754,111111)
		Huadong.Swipe_to_up (self, 4000)
		time.sleep(20)
if __name__ == '__main__':
    unittest.main()
