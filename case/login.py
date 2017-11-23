#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda

from iphoneinfo import shoujiinfo
device=shoujiinfo.connnect_ipad_device()
import time

def login():

	# 等待启动，设置程序休眠/防止手机反应慢卡死
	time.sleep(5)
	#点击账户
	device.find_elements_by_class_name ('android.widget.RadioButton') [3].click ()
	#点击更多
	time.sleep(2)
	device.find_elements_by_class_name('android.widget.TextView')[14].click()
	#退出
	time.sleep(2)
	device.find_elements_by_class_name('android.widget.Button')[0].click()
	#确定
	time.sleep(2)
	device.find_elements_by_class_name('android.widget.Button')[0].click()
	# 点击账户
	device.find_elements_by_class_name ('android.widget.RadioButton') [3].click ()
	#登录
	device.find_elements_by_class_name('android.view.View')[6].click()
	#登录账户
	device.find_elements_by_class_name ('android.widget.EditText') [0].clear()
	login_ip=device.find_elements_by_class_name('android.widget.EditText')[0]
	device.set_value(login_ip,'18519291259')
	device.find_elements_by_class_name('android.widget.Button')[0].click()
	#密码
	password=device.find_elements_by_class_name('android.widget.EditText')[0]
	device.set_value(password,'111111')
	device.find_elements_by_class_name('android.widget.Button')[0].click()
	#跳过手势密码
	device.find_elements_by_class_name('android.widget.ImageView')[9].click()
if __name__ == '__main__':
    login()
