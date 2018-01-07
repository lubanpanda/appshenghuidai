#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  84305510@qq.com
import unittest
import HTMLTestRunner
import time
from SHD_automation.device_info.device import *
from SHD_automation.panda_methods.my_methods import *
import datetime

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
		try:
			My_method.my_class_name_id_dianji(self,'android.view.View',5,'click',1)
			My_method.my_class_name_id_dianji(self,'android.view.View',7,'click',1)
			My_method.my_class_name_id_dianji(self,'android.view.View',9,'click',1)
			My_method.app_back(self,4)
		except:
			My_method.app_back(self)
		My_method.My_id(self,shouye_modul['新手指引'],'click',2)
		My_method.app_back(self)
		My_method.My_id(self,shouye_modul['邀请好友'],'click',2)
		My_method.app_back(self)
		My_method.My_id(self,shouye_modul['每日签到'],'click',2)
		My_method.app_back(self)
		time.sleep(2)
		Huadong.huadong(self,'上',6000)
		My_method.My_id(self,shouye_modul['消息公告'],'click')
		My_method.app_back(self)
		My_method.My_id(self,shouye_modul['帮助中心'],'click')
		My_method.app_back(self)


	def test_02_faxian(self):
		My_method.My_id(self,module_info['发现'],'click')
		My_method.My_id(self,faxian['平台数据'],'click',2)
		My_method.app_back(self)
		My_method.My_id(self,faxian['安全保障'],'click',2)
		for a in range (6):
			for i in range (2):
				My_method.my_class_name_id_dianji (self,'android.widget.Image', 1+a,'click',sleep_time = 1)
		My_method.app_back(self)
		My_method.My_id(self,faxian['积分商城'],'click',2)
		My_method.app_back(self)
		My_method.My_id(self,faxian['活动中心'],'click',2)
		My_method.app_back(self)
		My_method.my_class_name_id_dianji(self,faxian['更多'],6,'click')
		My_method.app_back(self)

	def test_03_zhanghu(self):
		My_method.My_id(self,module_info['账户'],'click')
		My_method.My_id(self,account['隐藏或显示'],'click')
		My_method.My_id(self,account['投资记录'],'click')
		My_method.My_id(self,account['截标记录'],'click')
		My_method.app_back(self,2)
		My_method.My_id(self,account['回款日历'],'click')
		My_method.app_back(self)
		My_method.My_id(self,account['资金记录'],'click')
		My_method.app_back(self)

	def test_04_shouhuo_addres(self):
		My_method.My_id(self,account['个人信息'],'click')
		My_method.My_id(self,account['地址管理'],'click')
		My_method.My_id(self,account['联系人'],"时寿阳")
		My_method.My_id(self,account['手机号'],'18519291259')
		add_info=My_method.My_id(self,account['收货地址格式'],'获取内容')
		logging.info(add_info)
		My_method.My_id(self,account['收货地址'],"北京市朝阳区林翠西里国际气候大厦三层")
		My_method.My_id(self,account['地址保存'],'click')
		My_method.app_back(self)
	# def test_05_tixian(self):
	# 	My_method.My_id(self,account['提现'],'click')
	# 	My_method.My_id(self,account['提现-下一步'],'click')
	# 	My_method.find_toast(self,"请输入提现金额")

if __name__ == '__main__':
	#unittest.main()
	suite = unittest.TestSuite ()
	nowtime = time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime ())
	suite.addTest(test_zhanghu ('test_01_shouye'))
	suite.addTest(test_zhanghu('test_02_faxian'))
	suite.addTest(test_zhanghu('test_03_zhanghu'))
	suite.addTest(test_zhanghu('test_04_shouhuo_addres'))
	#suite.addTest(test_zhanghu('test_05_tixian'))
	report_file = HTMLbaogao['报告地址'] + nowtime + "胜辉贷.html"
	fp = open (report_file, 'wb')
	baogao_info='简单的自动化'
	runner = HTMLTestRunner.HTMLTestRunner (stream = fp, title = "胜辉贷测试报告", description = baogao_info)
	runner.run (suite)
	fp.close ()
