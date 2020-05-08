#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

from appium import webdriver

#
# caps = {}
# caps["platformName"] = "Android"
# caps["deviceName"] = "3597ca050904"
# caps["platformVersion"] = "7.1.2"
# caps["sessionOverride"] = True
# caps["appPackage"] = "com.lmt"
# caps["newCommandTimeout"] = 600
# caps["appActivity"] = "com.lmt.MainActivity"
# caps["autoAcceptAlerts"] = True
# caps["noReset"] = True
# caps["unicodeKeyboard"] = True
# caps["resetKeyboard"] = True
#
# driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# driver.implicitly_wait(600)
#
# el1 = driver.find_element_by_accessibility_id("d0877691-2fd1-4b52-b154-ed3400192aa2")
# el1.click()
#

# driver.quit()

desired_caps = {}
desired_caps['automationName'] = 'XCUITest'  # Xcode8.2以上无UIAutomation,需使用XCUITest
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '13.4'  # '12.4.5'#'13.4'
desired_caps['deviceName'] = 'iPhone'  # 'panda  iPhone5s'#'iPhone'
desired_caps['bundleId'] = 'com.lmttrade.lmtpro'
desired_caps[
    'udid'] = 'e1fe8fde3664ab6320fd072a160dfe30b2f95ac6'  # "a4dd9d8df769060f8904558421042c70ddcdb396"#'e1fe8fde3664ab6320fd072a160dfe30b2f95ac6'
desired_caps['xcodeSigningId'] = "iPhone Developer"
desired_caps['xcodeOrgId'] = "SJJND89TJ5"  # SJJND89TJ5,9YE7XZT27H
desired_caps['newCommandTimeout'] = 3600  # 1 hour
desired_caps["sessionOverride"] = True

# 打开Appium服务器，start server后，尝试启动被测App
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
