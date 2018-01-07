#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/1/7 13:13
# @File : web_zidong.py
# @Software: PyCharm
import time
from selenium import webdriver

drive=webdriver.Chrome('/Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac/chromedriver')
drive.implicitly_wait(40)
drive.get('https://kingss.win/index.php/index/login/?')
#drive.find_element_by_xpath('//*[@id="kw"]').send_keys('appim')
#drive.find_element_by_xpath('//*[@placeholder="inputUsername"]').clear()

a=drive.find_element_by_xpath('//*[@placeholder="Username"]')
a.send_keys('panda')
print(a)
#drive.find_element_by_xpath('//*[@name="Password"]').clear()

b=drive.find_element_by_xpath('//*[@placeholder="Password"]')
b.send_keys('123456')
print(b)

c=drive.find_element_by_xpath('//*[@class="btn btn-lg btn-primary btn-block"]')
c.click()
print(c)
time.sleep(5)
