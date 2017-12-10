#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  84305510@qq.com
from appium import webdriver

def ios_devices():

	desired_caps = {
	    'platformName':'ios',
		'deviceName':'panda iPhone5s',
		'platformVersion':11.2,
		'bundleId': 'com.shenghuitouziguanli.shenghuidai',
	                }
	driver = webdriver.Remote ('http://127.0.0.1:4723/wd/hub', desired_caps)
	driver.implicitly_wait(60)
	driver.find_element_by_xpath('//XCUIElementTypeButton[@name="ok"]').click()
if __name__ == '__main__':
    ios_devices()