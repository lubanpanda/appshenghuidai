#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/1/16 10:59
import HTMLTestRunner
import time
from SHD_automation.device_info.device import star_app
from SHD_automation.panda_element.device_element import *
from SHD_automation.panda_methods.my_methods import My_method, logging, jietu
import unittest

# noinspection PyTypeChecker,PyUnresolvedReferences
class test_yaoqinghaoyou(unittest.TestCase,object):
	@classmethod
	def setUpClass (self):
		star_app.__init__ (self)
		star_app.setup (self)

	@classmethod
	def tearDownClass (self):
		self.driver.activate_ime_engine ('com.sohu.inputmethod.sogou.zui/.SogouIME')  # 恢复默认输入法
		star_app.tearDown (self)

	def test_yaoqing_haoyou(self):
		My_method.My_id (self, module_info ['首页'], 'click')
		My_method.My_id(self,shouye_modul['邀请好友'],'click')
		#先查看规则
		self.driver.implicitly_wait (20)
		try:
			My_method.my_class_name_id_dianji(self,'android.view.View',2,'click')
			My_method.my_class_name_id_dianji(self,'android.view.View',10,'click')
		except:
			logging.info("查看规则失败了")
		yaoqing_zhanji=['邀请人数','累计红包奖励','累计佣金奖励']
		for i in range(3):
			renshu=My_method.my_class_name_id_dianji(self,'android.view.View',6+i,'属性',"name")
			time.sleep(2)
			logging.info(f'{yaoqing_zhanji[i]}:{renshu[0]}')
		My_method.My_id(self,shouye_modul['邀请-好友'],'click')
		#就默认选择QQ分享了
		My_method.my_class_name_id_dianji(self,'android.widget.ImageButton',2,'click')
		try:
			self.driver.implicitly_wait (1)
			My_method.my_class_name_id_dianji(self,'android.widget.TextView',4,'click')
			My_method.My_id(self,shouye_modul['分享发送'],'click')
			My_method.My_id(self,'com.tencent.mobileqq:id/dialogLeftBtn','click')
			jietu.jietu_picture(self,"邀请好友成功")
			My_method.app_back(self)
		except:
			logging.info("QQ没有登录，分享失败")
			My_method.app_back(self,2)

if __name__ == '__main__':
	suite = unittest.TestSuite ()
	nowtime = time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime ())
	suite.addTest (test_yaoqinghaoyou ('test_yaoqing_haoyou'))
	report_file = HTMLbaogao ['报告地址'] + nowtime + "胜辉贷邀请好友.html"
	fp = open (report_file, 'wb')
	baogao_info ='邀请好友的信息'
	runner = HTMLTestRunner.HTMLTestRunner (stream = fp, title = "胜辉贷测试报告", description = baogao_info)
	runner.run (suite)
	fp.close ()