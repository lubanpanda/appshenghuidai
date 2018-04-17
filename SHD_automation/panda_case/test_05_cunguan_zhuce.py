#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/4/17 13:23

import HTMLTestRunner
import os
import unittest
import time
from SHD_automation.device_info.device import star_app
from SHD_automation.panda_element.device_element import *
from SHD_automation.panda_methods.my_methods import My_method, logging, myMethod

nowtime = time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime ())
# noinspection PyTypeChecker
class test_cunguan(unittest.TestCase,object):
	@classmethod
	def setUpClass (self):
		star_app.__init__ (self)
		star_app.setup(self)

	@classmethod
	def tearDownClass (self):
		self.driver.activate_ime_engine ('com.sohu.inputmethod.sogou.zui/.SogouIME')  # 恢复默认输入法
		star_app.tearDown (self)

	def test_01_zhuce(self):
		My_method.My_id(self,module_info['存管注册'],'click')
		My_method.My_id(self,zhuce['账号'],myMethod.randomTel(self))
		My_method.My_id(self,account['注册-下一步'],'click')
		My_method.My_id(self,account['验证码'],123456)
		My_method.My_id(self,account['登录密码'],123456)
		My_method.My_id(self,account['确定'],'click')
		My_method.My_id(self,zhuce['跳过'],'click')

	def test_02_qianyue(self,names='张三'):
		My_method.My_id(self,module_info['账户'],'click')
		My_method.My_id(self,cunguan["充值"],'click')
		KT_cunguan=My_method.My_id(self,cunguan['立即开通'],'获取元素')
		if KT_cunguan:
			logging.info ('存管账户未开通')
			My_method.My_id (self, cunguan ['立即开通'], 'click')
			My_method.My_id (self, 'name', names)
			My_method.My_id (self, 'identity', myMethod.randomID (self))
			My_method.my_class_name_id_dianji (self, 'android.view.View', 9, 'click')
			chenggong = My_method.my_class_name_id_dianji (self, 'android.widget.Button', 0, '获取元素')
			if chenggong:
				logging.info ('开户成功')
				My_method.my_class_name_id_dianji (self, 'android.widget.Button', 0, 'click')

			else:
				logging.info ('开户失败')
		else:
			logging.info('已经开通存管账户')

	def test_03_bangka(self):
		My_method.My_id(self,module_info['账户'],'click')
		My_method.My_id(self,cunguan["充值"],'click')
		My_method.my_class_name_id_dianji(self,'android.widget.EditText',1,'click')
		My_method.my_class_name_id_dianji(self,'android.view.View',36,'click')
		My_method.my_class_name_id_dianji(self,'android.view.View',14,myMethod.bankId(self))
		My_method.my_class_name_id_dianji(self,'android.view.View',17,'click')
		My_method.my_class_name_id_dianji(self,'android.view.View',36,'click')
		My_method.my_class_name_id_dianji(self,'android.view.View',20,'北京')
		My_method.my_class_name_id_dianji(self,'android.view.View',23,'北京')
		My_method.my_class_name_id_dianji(self,'android.view.View',26,myMethod.randomTel(self))
		os.popen ('adb shell input swipe 50 1000 50 0 100')
		My_method.my_class_name_id_dianji(self,'android.view.View',28,'click')
		logging.info('绑卡成功')

if __name__ == '__main__':
	suite = unittest.TestSuite ()
	suite.addTest (test_cunguan ('test_01_zhuce'))
	suite.addTest (test_cunguan ('test_02_qianyue'))
	suite.addTest (test_cunguan ('test_03_bangka'))
	report_file = HTMLbaogao ['报告地址'] + nowtime + "胜辉贷存管.html"
	fp = open (report_file, 'wb')
	baogao_info = '胜辉贷存管签约绑卡注册'
	runner = HTMLTestRunner.HTMLTestRunner (stream = fp, title = "胜辉贷存管测试报告", description = baogao_info)
	runner.run (suite)
	fp.close ()