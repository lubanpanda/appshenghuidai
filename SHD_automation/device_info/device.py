#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  84305510@qq.com
from SHD_automation.panda_element import *
from appium import webdriver
import logging
from SHD_automation.panda_element.device_element import *
from SHD_automation.panda_log.log import log
from SHD_automation.panda_methods.my_methods import Pingmu_unlock_the_screen



class star_app(object):
	def __init__(self):
		log()
		self.logging=logging.getLogger()
		Pingmu_unlock_the_screen()
		self.jiesuo=Pingmu_unlock_the_screen.pingmu_jiesuo(self)

	def setup(self):
		desired_caps = {}
		desired_caps ['platformName'] = device_info['platformName']
		desired_caps ['platformVersion'] = device_info['platformVersion']
		desired_caps ['sessionOverride']=device_info['sessionOverride']
		desired_caps ['deviceName'] = device_info['deviceName']
		desired_caps ['appPackage'] = device_info['appPackage']
		desired_caps ['appActivity'] = device_info['appActivity']
		desired_caps ['noReset'] = device_info['noReset']
		desired_caps ['unicodekeyboard'] = device_info['unicodeKeyboard']
		desired_caps ['resetKeyboard']=device_info['resetKeyboard']
		desired_caps ['newCommandTimeout'] = device_info['newCommandTimeout']
		self.driver = webdriver.Remote ('http://127.0.0.1:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(30)
		self.logging.info(self.driver)


	def tearDown (self):
		self.driver.quit ()