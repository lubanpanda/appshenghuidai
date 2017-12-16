#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
from iphoneinfo import shoujiinfo
device=shoujiinfo.connnect_ipad_device()
import time
def All_shouye():
	'''
	首页的四个小模块查看
	:return:
	'''
	device.implicitly_wait(30)
	u'投资攻略'
	# device.find_elements_by_class_name('android.widget.TextView')[0].click()
	# time.sleep(2)
	# for i in range(3,10,2):
	# 	device.find_elements_by_class_name('android.view.View')[i].click()
	# for a in range(5):
	# 	device.back()
	# time.sleep(2)
	u'邀请好友'
	device.find_elements_by_class_name('android.widget.TextView')[2].click()
	device.find_element_by_id('com.yourenkeji.shenghuidai:id/webView_bt_share').click()
	time.sleep(3)
	#'点击QQ'
	device.find_elements_by_class_name('android.widget.ImageButton')[2].click()
	time.sleep(3)
	'分享给我的电脑'
	device.find_elements_by_class_name('android.widget.RelativeLayout')[5].click()
	'发送'
	device.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()

	'返回'
	device.find_element_by_id('com.tencent.mobileqq:id/dialogLeftBtn').click()

	u'每日签到'
	device.find_elements_by_class_name('android.widget.TextView')[3].click()
	u'签到'
	qiandao = device.find_elements_by_class_name ('android.view.View')
	if qiandao and len (qiandao) == 53:

		print ('签到成功')
	else:
		device.find_elements_by_class_name ('android.view.View')[53].click ()
		print ('已经签到完成')
	u'签到规则'
	device.find_elements_by_class_name('android.widget.ImageView')[1].click()
	device.back()
	device.back()
if __name__ == '__main__':
    All_shouye()