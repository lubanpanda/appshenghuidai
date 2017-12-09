#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
from time import sleep
from iphoneinfo import shoujiinfo
device=shoujiinfo.connnect_ipad_device()
import time
import threading
import os
def timeout():
	'''
	支付密码超时处理
	:return:
	'''
	print("输入超时，默认不做提现处理")
	other()


def all_account(money):
	'''
	账户页面的操作
	:param money:提现的金额
	:return:
	'''
	device.implicitly_wait(30)
	device.find_elements_by_class_name('android.widget.RadioButton')[3].click()
	'隐藏金额'
	device.find_element_by_id('com.yourenkeji.shenghuidai:id/my_eyes_checkbox').click()
	'账户信息'
	device.find_element_by_id('com.yourenkeji.shenghuidai:id/imageView1').click()
	'账户余额'
	device.find_element_by_id('com.yourenkeji.shenghuidai:id/my_zongzichan_img_right').click()
	'冻结金额'
	device.find_element_by_id('com.yourenkeji.shenghuidai:id/my_zongzichan_img_dongjieyue').click()
	device.find_element_by_id('com.yourenkeji.shenghuidai:id/positiveButton').click()
	time.sleep(2)
	device.back()
	#投资记录
	device.find_elements_by_class_name('android.widget.TextView')[5].click()
	sleep(2)
	device.find_elements_by_class_name('android.widget.TextView')[2].click()
	device.back()
	device.back()
	#回款日历
	device.find_elements_by_class_name('android.widget.TextView')[6].click()
	device.back()
	t = threading.Timer (10.0, timeout)
	t.start ()
	select_tixian = int (input ("体现输入1，不提醒输入2，请在10S内输入:"+os.linesep))
	if  select_tixian==1:
		#体现
		t.cancel()
		device.find_elements_by_class_name('android.widget.TextView')[8].click()
		tixian_money=device.find_elements_by_class_name('android.widget.RelativeLayout')[2]
		tixian_money.click()
		tixian_money.send_keys(money)
		while True:
			if money<0:
				print("请输入正确金额")
				break
			elif money<100:
				print("提现金额最低为100元")
				break
			else:
				print("金额输入正确，请进行下一步操作")
				break
		device.find_elements_by_class_name('android.widget.Button')[0].click()
		for i in range (6):
			new_password = device.find_elements_by_class_name ('android.widget.Button') [i]
			new_password.click ()
		time.sleep(2)
		device.find_elements_by_class_name('android.widget.Button')[0].click()

	else:
		t.cancel()
		print("不做提现动作")

	other()
def other():
	'''
	资金记录到更多
	:return:
	'''
	#资金记录
	time.sleep(2)
	device.find_elements_by_class_name('android.widget.TextView')[9].click()
	device.back()
	#安全管理
	device.find_elements_by_class_name('android.widget.TextView')[12].click()
	device.find_elements_by_class_name('android.widget.RelativeLayout')[1].click()
	#记得支付密码
	device.find_elements_by_class_name('android.widget.RelativeLayout')[2].click()
	yuan_key=device.find_elements_by_class_name('android.widget.EditText')[0]
	device.set_value(yuan_key,123456)
	new_key=device.find_elements_by_class_name('android.widget.EditText')[1]
	device.set_value(new_key,123456)
	new_key_too=device.find_elements_by_class_name('android.widget.EditText')[2]
	device.set_value(new_key_too,123456)
	device.find_elements_by_class_name('android.widget.Button')[0].click()
	time.sleep(2)
	#设置手势密码
	time.sleep(2)
	device.find_elements_by_class_name('android.widget.RelativeLayout')[2].click()
	device.back()
	device.back()
	time.sleep(2)
	device.find_elements_by_class_name('android.widget.TextView')[13].click()
	device.back()
	time.sleep(2)
	device.find_elements_by_class_name('android.widget.TextView')[14].click()
	device.back()
if __name__ == '__main__':
    all_account(100)