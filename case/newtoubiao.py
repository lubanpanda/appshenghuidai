#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
import time
from iphoneinfo import shoujiinfo
device=shoujiinfo.connnect_ipad_device()

def new_toubiao():
	'''
	投资新手标
	:return:
	'''
	device.implicitly_wait (10)
	device.find_elements_by_class_name('android.widget.RelativeLayout')[1].click()
	touzi_money=device.find_elements_by_class_name('android.widget.EditText')[0]
	device.set_value(touzi_money,1000)
	device.find_elements_by_class_name('android.widget.Button')[1].click()
	new_biao_youhui=device.find_elements_by_class_name('android.widget.TextView')[21].click()
	if new_biao_youhui:
		print ("可以点击使用优惠券，请确认是否是新手或了解业务需求")
	else:
		print ("验证正确，不能使用优惠券")
	new_buy=device.find_elements_by_class_name('android.widget.Button')[0].click()
	if new_buy:
		print("你不是新手，可以购买")

	else:
		print("你已经不是新手了，不能购买新手标了")
	device.back()
	device.back()
if __name__ == '__main__':
    new_toubiao()
