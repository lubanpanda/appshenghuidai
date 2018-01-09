#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/1/9 09:55
# @File : test_registered.py
# @Software: PyCharm
'''
用于用户的注册操作
'''
from SHD_automation.device_info.device import *


class Zhuce(object):


	def setUpClass (self):
		log()
		star_app.setup (self)


	def tearDownClass (self):
		star_app.tearDown (self)

	def zhuce(self):
		My_method.My_id(self,module_info['账户'],'click')
		My_method.My_id(self,zhuce['注册'],'click')
		My_method.My_id(self,zhuce['账号'],15201019885)
