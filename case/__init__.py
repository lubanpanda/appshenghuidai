#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
from appium import webdriver
import time
import os
app_path='/Users/yuchengtao/Downloads/boluolicai.app'
desired_caps = {
			'platformName': 'iOS',
			'deviceName': 'iPhone Simulator',
			'platformVersion': '11.2',
			#'sessionOverride': True,
			'sessionOverride': True,
			'app': app_path


		}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.implicitly_wait(30)
driver.find_element_by_ios_class_chain()