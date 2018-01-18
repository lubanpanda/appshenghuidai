#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/1/17 14:08
import HTMLTestRunner
import unittest
import time
from appium import webdriver
from SHD_automation.device_info.device import star_app
from SHD_automation.panda_element.device_element import *
from SHD_automation.panda_methods.my_methods import My_method, logging, jietu


# noinspection PyTypeChecker
class test_fengxian(unittest.TestCase,object):
	@classmethod
	def setUpClass (self):
		star_app.__init__ (self)
		desired_caps = {}
		desired_caps ['platformName'] = device_info ['platformName']
		desired_caps ['platformVersion'] = device_info ['platformVersion']
		desired_caps ['sessionOverride'] = device_info ['sessionOverride']
		desired_caps ['deviceName'] = device_info ['deviceName']
		desired_caps ['appPackage'] = device_info ['appPackage']
		desired_caps ['appActivity'] = device_info ['appActivity']
		desired_caps ['noReset'] = device_info ['noReset']
		desired_caps ['unicodeKeyboard'] = device_info ['unicodeKeyboard']
		desired_caps ['resetKeyboard'] = device_info ['resetKeyboard']
		desired_caps ['newCommandTimeout'] = device_info ['newCommandTimeout']
		desired_caps ['automationName'] = 'UIAutomator2'
		self.driver = webdriver.Remote ('http://127.0.0.1:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait (20)

	@classmethod
	def tearDownClass (self):
		self.driver.activate_ime_engine ('com.sohu.inputmethod.sogou.zui/.SogouIME')  # 恢复默认输入法
		star_app.tearDown (self)

	def test_01_fengxian(self):
		My_method.My_id (self, module_info ['首页'], 'click')
		logging.info("首先获取新手标的详细信息")
		xinshou_info=['标得名称：','性质：','活动','预期年化收益：','活动加息:','投资期限：','可投金额：']
		xinshou_jieguo=[]
		for i in range(6):
			biao_name=My_method.my_class_name_id_dianji(self,'android.widget.TextView',7+i,'text')
			xinshou_jieguo.append(biao_name[0])
		info=dict(map(lambda x,y:[x,y], xinshou_info,xinshou_jieguo))
		logging.info(f'标得详细信息如下：{info}')
		My_method.My_id(self,'com.yourenkeji.shenghuidai:id/buy_now_tv','click')  #点击 立即投资
		My_method.My_id(self,'com.yourenkeji.shenghuidai:id/bid_detals_et_bidMoney',100) #就是看看可不可以投资
		My_method.My_id(self,'com.yourenkeji.shenghuidai:id/bid_detals_bt_bid','click')
		My_method.My_id(self,'com.yourenkeji.shenghuidai:id/bid_buy_bt','click')    #立即购买
		jietu.jietu_picture(self,"新手标")
		logging.info("你已经不是新手了，不能在投资新手标了")


if __name__ == '__main__':
	suite = unittest.TestSuite ()
	nowtime = time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime ())
	suite.addTest (test_fengxian ('test_01_fengxian'))
	report_file = HTMLbaogao ['报告地址'] + nowtime + "胜辉贷新手标.html"
	fp = open (report_file, 'wb')
	baogao_info ='新手标测试'
	runner = HTMLTestRunner.HTMLTestRunner (stream = fp, title = "胜辉贷测试报告", description = baogao_info)
	runner.run (suite)
	fp.close ()