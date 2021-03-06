#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  84305510@qq.com
import unittest
import HTMLTestRunner
import re
import time
import os
import random
from SHD_automation.device_info.device import star_app
from SHD_automation.panda_element.device_element import *
from SHD_automation.panda_methods.my_methods import My_method, logging, jietu
# noinspection PyTypeChecker
class test_zhanghu(unittest.TestCase,object):
	@classmethod
	def setUpClass(self):
		star_app.__init__(self)
		star_app.setup(self)

	@classmethod
	def tearDownClass(self):
		self.driver.activate_ime_engine ('com.sohu.inputmethod.sogou.zui/.SogouIME')  # 恢复默认输入法
		star_app.tearDown(self)


	def test_01_shouye(self):
		My_method.My_id(self,module_info['首页'],'click')
		My_method.My_id(self,shouye_modul['榜上有名'],'click',3)
		My_method.app_back(self)
		My_method.My_id(self,shouye_modul['新手指引'],'click',2)
		My_method.app_back(self)
		My_method.My_id(self,shouye_modul['邀请好友'],'click',2)
		My_method.app_back(self)
		My_method.My_id(self,shouye_modul['每日签到'],'click',2)
		while True:
			try:
				while True:
					try:
						huoqu_jifen=My_method.my_class_name_id_dianji(self,'android.view.View',1,'属性',"name")
						time.sleep (3)
						logging.info (huoqu_jifen [0])
						break
					except:
						continue
				b = My_method.my_class_name_id_dianji (self, 'android.view.View', 53, 'click')
				if b:
					self.driver.implicitly_wait (3)
					try:
						qiandao_jifen = My_method.my_class_name_id_dianji (self, 'android.widget.Button', 0, '属性', "name", 4)
						My_method.my_class_name_id_dianji (self, 'android.widget.Button', 0, 'click')
						logging.info (qiandao_jifen[0])
						break
					except:
						logging.info ("已经签到了")
						break
			except:
				My_method.yiwai_login(self)
				continue
		My_method.app_back(self)


	def test_02_faxian(self):
		My_method.My_id(self,module_info['发现'],'click')
		My_method.My_id(self,faxian['平台数据'],'click',2)
		My_method.app_back(self)
		My_method.My_id(self,faxian['安全保障'],'click',2)
		for a in range (6):
			for i in range (2):
				My_method.my_class_name_id_dianji (self, 'android.widget.Image', 1 + a, 'click')
		My_method.app_back(self)
		My_method.My_id (self, faxian['积分商城'], 'click')
		while True:
			# noinspection PyUnresolvedReferences
			self.driver.implicitly_wait (3)
			try:
				My_method.yiwai_login (self)
				My_method.My_id (self, module_info ['发现'], 'click')
				My_method.My_id (self, faxian ['积分商城'], 'click', 2)
				continue
			except:
				jifen = My_method.my_class_name_id_dianji (self, 'android.view.View', 2, '属性', "name")
				jifen_i = re.findall ('[A-Za-z0-9]+', jifen [0])
				jifen_info = jifen_i [0]
				logging.info (f'积分:{jifen_info}')
				os.popen ('adb shell input swipe 50 1000 50 750 100')#向上滑动至合适距离
				p = 7
				zong_jifen = []

				for i in range (8):
					jifen_op = My_method.my_class_name_id_dianji (self, 'android.view.View', p, '属性', "name")
					jifen_io = re.findall ('[A-Za-z0-9]+', jifen_op [0])
					zong_jifen.append (jifen_io [0])
					p += 3
				logging.info (zong_jifen)
				suiji_list_len = [7]
				suiji_list = 7
				for w in range (7):
					suiji_list += 3
					suiji_list_len.append (suiji_list)
				suiji_list_to = random.randrange (7, 28, 3)
				weizhi_info = suiji_list_len.index (suiji_list_to)
				My_method.my_class_name_id_dianji (self, 'android.view.View', suiji_list_to, 'click',3)
				weizhi_jifen = zong_jifen[weizhi_info]
				if weizhi_jifen<=jifen_info:
					My_method.my_class_name_id_dianji(self,'android.view.View',22,'click',2)
					My_method.my_class_name_id_dianji(self,'android.widget.Button',1,'click')
					jietu.jietu_picture (self, "兑换积分")
					My_method.my_class_name_id_dianji(self,'android.widget.Button',0,'click')
					logging.info ('兑换成功')

					My_method.app_back(self,2)

				else:
					logging.info('兑换失败')
					My_method.app_back(self,2)
				break
		My_method.My_id(self,faxian['活动中心'],'click',2)
		My_method.app_back(self)
		My_method.my_class_name_id_dianji(self,faxian['更多'],6,'click')
		My_method.app_back(self)

	def test_03_shouhuo_addres(self):
		My_method.My_id (self, module_info ['账户'], 'click')
		My_method.My_id (self, account ['个人中心'], 'click')
		My_method.My_id(self,account['地址管理'],'click')
		My_method.My_id(self,account['联系人'],"时寿阳")
		My_method.My_id(self,account['手机号'],'18519291259')
		add_info=My_method.My_id(self,account['收货地址格式'],'获取内容')
		logging.info(add_info)
		My_method.My_id(self,account['收货地址'],"北京市朝阳区林翠西里国际气候大厦三层")
		My_method.My_id(self,account['地址保存'],'click')
		My_method.app_back(self)

if __name__ == '__main__':
	suite = unittest.TestSuite ()
	nowtime = time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime ())
	suite.addTest(test_zhanghu ('test_01_shouye'))
	suite.addTest(test_zhanghu('test_02_faxian'))
	suite.addTest(test_zhanghu('test_03_shouhuo_addres'))
	report_file = HTMLbaogao['报告地址'] + nowtime + "胜辉贷.html"
	fp = open (report_file, 'wb')
	baogao_info='内容包括：\n' \
	            '一.首页\n' \
	            '1.首页的投资攻略模块\n' \
	            '2.新手指引模块\n' \
	            '3.每日签到模块\n' \
	            '4.邀请好友模块带完成\n' \
	            '5.帮助中心\n' \
	            '二.发现模块\n' \
	            '1.平台数据\n' \
	            '2.安全保障\n' \
	            '3.积分商城\n' \
	            '4.活动中心\n' \
	            '三.账户模块\n' \
	            '1.除【提现，充值】外的所以功能'
	runner = HTMLTestRunner.HTMLTestRunner (stream = fp, title = "胜辉贷测试报告", description = baogao_info)
	runner.run (suite)
	fp.close ()
