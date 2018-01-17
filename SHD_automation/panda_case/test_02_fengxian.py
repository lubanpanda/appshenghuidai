#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/1/15 11:13

import HTMLTestRunner
import random
import unittest
import time
from SHD_automation.device_info.device import star_app
from SHD_automation.panda_element.device_element import *
from SHD_automation.panda_methods.my_methods import My_method, logging, myMethod
import os

# noinspection PyTypeChecker
class test_fengxian(unittest.TestCase,object):
	@classmethod
	def setUpClass (self):
		star_app.__init__ (self)
		star_app.setup (self)

	@classmethod
	def tearDownClass (self):
		self.driver.activate_ime_engine ('com.sohu.inputmethod.sogou.zui/.SogouIME')  # 恢复默认输入法
		star_app.tearDown (self)

	def test_01_fengxian(self):
		My_method.My_id (self, module_info ['账户'], 'click')
		os.popen ('adb shell input swipe 50 1000 50 750 100')
		My_method.My_id(self,account['更多'],'click')
		My_method.My_id(self,account['风险评估'],'click')
		cishu=1
		while cishu<=10:
			timu=My_method.my_class_name_id_dianji(self,'android.view.View',3,'属性',"name") #答题的题目
			time.sleep(2)
			logging.info(f'题目:{timu[0]}')
			xuan_xiang=random.randint(4,7)
			xuanxiang_info=My_method.my_class_name_id_dianji(self,'android.view.View',xuan_xiang,'属性',"name") #获得选项信息
			logging.info(f'选项：{xuanxiang_info[0]}')
			My_method.my_class_name_id_dianji(self,'android.view.View',xuan_xiang,'click')
			if cishu <= 9:
				self.driver.find_element_by_xpath('//android.view.View[@content-desc="下一题"]').click()
				cishu+=1
			elif cishu==10:
				self.driver.find_element_by_xpath ('//android.view.View[@content-desc="完成"]').click ()
				break
		pinggu_jieguo=My_method.my_class_name_id_dianji(self,'android.view.View',2,'属性',"name")#获得评估完成的信息
		time.sleep(2)
		logging.info(f'评估结果:{pinggu_jieguo[0]}')
		self.driver.find_element_by_xpath ('//android.widget.Button[@content-desc="去理财"]').click ()
if __name__ == '__main__':
    unittest.main()