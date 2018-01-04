#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  84305510@qq.com
import unittest
import HTMLTestRunner
import time
from SHD_automation.device_info.device import *
from SHD_automation.panda_methods.my_methods import *


# noinspection PyTypeChecker
class test_zhanghu(unittest.TestCase,object):
	@classmethod
	def setUpClass(self):
		star_app.__init__(self)
		star_app.setup(self)

	@classmethod
	def tearDownClass(self):
		star_app.tearDown(self)


	def test_01_shouye(self):
		My_method.My_id(self,module_info['首页'],'click')
		My_method.My_id(self,shouye_modul['投资攻略'],'click',3)
		My_method.my_class_name_id_dianji(self,'android.view.View',5,'click')
		My_method.my_class_name_id_dianji(self,'android.view.View',7,'click')
		My_method.my_class_name_id_dianji(self,'android.view.View',9,'click')
		My_method.app_back(self,4)
		My_method.My_id(self,shouye_modul['新手指引'],'click',2)
		My_method.app_back(self)
		My_method.My_id(self,shouye_modul['邀请好友'],'click',2)
		My_method.app_back(self)
		My_method.My_id(self,shouye_modul['每日签到'],'click',2)
		My_method.app_back(self)

	def test_02_faxian(self):
		My_method.My_id(self,module_info['发现'],'click')
		My_method.My_id(self,faxian['平台数据'],'click',2)
		My_method.app_back(self)
		My_method.My_id(self,faxian['安全保障'],'click',2)
		for a in range (6):
			# noinspection PyAssignmentToLoopOrWithParameter
			for i in range (2):
				My_method.my_class_name_id_dianji (self,'android.widget.Image', 1+a,'click',sleep_time = 2)
		My_method.app_back(self)
		My_method.My_id(self,faxian['积分商城'],'click',2)
		My_method.app_back(self)
		My_method.My_id(self,faxian['活动中心'],'click',2)
		My_method.app_back(self)
		My_method.my_class_name_id_dianji(self,faxian['更多'],6,'click')
		My_method.app_back(self)

	def test_03_zhanghu_xiangqing(self):
		My_method.My_id(self,module_info['账户'],'click')
		My_method.My_id(self,account['隐藏或显示'],'click')
		My_method.My_id(self,account['投资记录'],'click')
		My_method.My_id(self,account['截标记录'],'click')
		My_method.app_back(self,2)
		My_method.My_id(self,account['回款日历'],'click')
		My_method.app_back(self)
		My_method.My_id(self,account['资金记录'],'click')
		My_method.app_back(self)


if __name__ == '__main__':
	unittest.main()
	# suite = unittest.TestSuite ()
	# nowtime = time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime ())
	# suite.addTest (test_zhanghu ('test_01_login'))
	# suite.addTest(test_zhanghu('test_02_zhanghu_xiangqing'))
	# report_file = HTMLbaogao['报告地址'] + nowtime + "appium_report.html"
	# fp = open (report_file, 'wb')
	# runner = HTMLTestRunner.HTMLTestRunner (stream = fp, title = "appium测试报告", description = '新增一条笔记并保存')
	# runner.run (suite)
	# fp.close ()
