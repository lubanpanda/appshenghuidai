#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda

import unittest
import HTMLTestRunner
import time
from iphoneinfo import shoujiinfo
from appium import webdriver
from fengfan_unittest.feng_test_method.method import *
class test0(unittest.TestCase,object):

	def setUp(self):
		shoujiinfo.__init__(self)
		shoujiinfo.setUp(self)
	def tearDown(self):
		shoujiinfo.tearDown (self)
	def test_log(self):
		# 点击账户
		self.device.find_elements_by_class_name ('android.widget.RadioButton') [3].click ()

		# 点击更多

		print ('准备开始切换账户了')
		self.device.find_elements_by_class_name ('android.widget.TextView') [14].click ()
		self.device.find_elements_by_class_name ('android.widget.Button') [0].click ()
		# 确定

		self.device.find_elements_by_class_name ('android.widget.Button') [0].click ()
		# 点击账户
		self.device.find_elements_by_class_name ('android.widget.RadioButton') [3].click ()
		# 登录
		self.device.find_element_by_id('com.yourenkeji.shenghuidai:id/bt_dilog_login').click ()
		# 登录账户
		self.device.find_elements_by_class_name ('android.widget.EditText') [0].clear ()
		login_ip = self.device.find_elements_by_class_name ('android.widget.EditText') [0]
		self.device.set_value (login_ip, '18519291259')
		self.device.find_elements_by_class_name ('android.widget.Button') [0].click ()
		# 密码
		password = self.device.find_elements_by_class_name ('android.widget.EditText') [0]
		self.device.set_value (password, '111111')
		self.device.find_elements_by_class_name ('android.widget.Button') [0].click ()
		# 跳过手势密码
		self.device.find_element_by_id('com.yourenkeji.shenghuidai:id/img_cancel').click()
if __name__ == '__main__':
	suite = unittest.TestSuite ()
	nowtime = time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime ())
	suite.addTest (test0 ('test_log'))
	report_file = "/Users/yuchengtao/Desktop/胜辉贷/"+nowtime+"appium_report.html"

	fp = open (report_file,'wb')

	runner = HTMLTestRunner.HTMLTestRunner (stream = fp, title = "appium测试报告", description ='新增一条笔记并保存')

	runner.run (suite)

	fp.close ()