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
import HTMLTestRunner
import unittest
import time
from SHD_automation.device_info.device import star_app
from SHD_automation.panda_element.device_element import *
from SHD_automation.panda_methods.my_methods import My_method, logging
from fengfan_unittest.feng_test_method.method import myMethod

# noinspection PyTypeChecker
class Zhuce(unittest.TestCase):
	def setUp (self):
		star_app.__init__(self)
		star_app.setup (self)

	def tearDown (self):
		star_app.tearDown (self)

	def test_zhuce(self,yaoqingren=0,phone=''):
		My_method.My_id(self,module_info['账户'],'click')
		My_method.My_id(self,zhuce['注册'],'click')
		phone_number=myMethod.randomTel(self)
		My_method.My_id(self,zhuce['账号'],phone_number)
		My_method.My_id(self,account['注册-下一步'],'click')
		yanzhengma=My_method.My_id(self,account['验证码'],'获取内容')
		yanzhengma_int='000000'
		My_method.My_id(self,account['验证码'],yanzhengma_int)
		logging.info(f'{yanzhengma[0]}:000000')
		pawwoed=123456
		logio_password=My_method.My_id(self,account['登录密码'],'获取内容')
		My_method.My_id(self,account['登录密码'],pawwoed)
		logging.info(f'{logio_password[0]}:{pawwoed}')
		passwoed_too=pawwoed
		passpod=My_method.My_id(self,account['确认密码'],'获取内容')
		My_method.My_id(self,account['确认密码'],passwoed_too)
		logging.info(f'{passpod[0]}:{passwoed_too}')
		#邀请人可自己选择,0是不邀请，1是可邀请
		if yaoqingren==0:
			logging.info('不填写邀请人')
		else:
			tuijianren=My_method.My_id(self,account['推荐人'],'获取内容')
			My_method.My_id(self,account['推荐人'],phone)
			logging.info(f'{tuijianren}:{phone}')
		My_method.My_id(self,account['确定'],'click')
		My_method.My_id(self,zhuce['跳过'],'click')
if __name__ == '__main__':
	unittest.main()
    # suite = unittest.TestSuite ()
    # nowtime = time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime ())
    # suite.addTest (Zhuce ('test_zhuce'))
    # report_file = HTMLbaogao ['报告地址'] + nowtime + "胜辉贷注册.html"
    # fp = open (report_file, 'wb')
    # baogao_info = '随机生成一个11位的手机号来进行模拟用户注册的操作'
    # runner = HTMLTestRunner.HTMLTestRunner (stream = fp, title = "注册测试报告", description = baogao_info)
    # runner.run (suite)
    # fp.close ()