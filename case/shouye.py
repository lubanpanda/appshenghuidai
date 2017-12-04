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
	device.find_elements_by_class_name('android.widget.TextView')[0].click()
	time.sleep(2)
	device.back()
	u'新手指引'
	device.find_elements_by_class_name('android.widget.TextView')[1].click()
	time.sleep(2)
	device.back()
	u'邀请好友'
	device.find_elements_by_class_name('android.widget.TextView')[2].click()
	device.find_elements_by_class_name('android.widget.Button')[0].click()
	device.back()
	device.find_elements_by_class_name('android.widget.Button')[1].click()
	device.back()
	device.back()
	u'每日签到'
	device.find_elements_by_class_name('android.widget.TextView')[3].click()
	u'签到'
	device.find_elements_by_class_name('android.view.View')[53].click()
	u'签到规则'
	device.find_elements_by_class_name('android.widget.ImageView')[1].click()
	device.back()
	device.back()
if __name__ == '__main__':
    All_shouye()