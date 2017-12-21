#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda

import unittest
import HTMLTestRunner
import time
from appium import webdriver
class test0(unittest.TestCase):
	def setUp(self):
		desired_caps = {
			'platformName': 'Android',
			'deviceName': '3cdbb8e5',
			'platformVersion': '7.0',
			'sessionOverride': True,
			'appPackage': 'com.yourenkeji.shenghuidai',
			'newCommandTimeout': 600,
			'appActivity': 'com.delevin.shenghuidai.welcome.WelcomeActivity',
			'autoAcceptAlerts': True,
			'noReset': True,
			'unicodeKeyboard': True,  # 设置appium输入法后就不会弹默认的系统输入法了
			'resetKeyboard': False,  # 重置系统输入法
		                }
		self.device=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		self.device.implicitly_wait(20)
	def tearDown(self):
		pass
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