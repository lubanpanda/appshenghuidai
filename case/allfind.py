#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  84305510@qq.com
from iphoneinfo import shoujiinfo
import unittest
import time
import HTMLTestRunner
from case import redraw
class test1(unittest.TestCase):
	def setUp(self):
		self.device=shoujiinfo.connnect_ipad_device()

		self.device.implicitly_wait (30)
	def tearDown(self):
		pass
	def test_all_find(self):
		self.device.find_elements_by_class_name('android.widget.RadioButton')[2].click()
		self.device.find_elements_by_class_name('android.widget.ImageView')[0].click()
		u'平台数据'
		self.device.find_elements_by_class_name('android.widget.TextView')[0].click()
		time.sleep(2)
		self.device.back()
		u'安全保障'
		self.device.find_elements_by_class_name ('android.widget.TextView') [1].click ()
		for i in range(6):
			for a in range(2):
				self.device.find_elements_by_class_name('android.widget.Image')[1+i].click()
		self.device.back()
		u'积分商城'
		self.device.find_element_by_id('com.yourenkeji.shenghuidai:id/jifenshangcheng').click()
		u'查看积分'
		self.device.find_elements_by_class_name('android.widget.Image')[0].click()
		self.device.back()
		for i in range(8):
			if i >= 5:
				try:
					redraw.swipe_to_up(1000)
				except Exception as e:
					print(e)
				self.device.find_elements_by_class_name('android.widget.Image')[2+i].click()
				time.sleep(2)
				self.device.back()
			else:
				self.device.find_elements_by_class_name ('android.widget.Image') [2 + i].click ()
				time.sleep(2)
				self.device.back()

if __name__ == '__main__':
	suite = unittest.TestSuite ()

	suite.addTest (test1 ('test_all_find'))
	report_file = "/Users/yuchengtao/Desktop/胜辉贷/faxian.html"

	fp = open (report_file, 'wb')
	print(fp)
	runner = HTMLTestRunner.HTMLTestRunner (stream = fp, title = "发现报告", description = '新增一条笔记并保存')

	runner.run (suite)

	fp.close ()