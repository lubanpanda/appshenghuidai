#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
from appium import webdriver
def connnect_ipad_device():
	'''
	定义测试平台的属性
	:return: device及参数
	'''
	try:

		import time
		desired_caps = {
			'platformName': 'Android',
			'deviceName': '3cdbb8e5',
			'platformVersion': '7.0',
			'sessionOverride': True,
			'appPackage': 'com.yourenkeji.shenghuidai',
			'newCommandTimeout': 600,
			'appActivity': 'com.delevin.shenghuidai.welcome.WelcomeActivity',
			'autoAcceptAlerts': True,
			'noReset':True,   #不要在会话前重置应用状态。默认值false
			'unicodeKeyboard':True,#设置appium输入法后就不会弹默认的系统输入法了
			'resetKeyboard':False, #重置系统输入法

		}
		driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		return driver
	except Exception as e:
		print(e)
if __name__ == '__main__':
    device=connnect_ipad_device()