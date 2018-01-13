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
drive.find_element_by_xpath('//*[@placeholder="Username"]').send_keys('panda')
drive.find_element_by_xpath('//*[@placeholder="Password"]').send_keys('123456')
drive.find_element_by_xpath('//*[@class="btn btn-lg btn-primary btn-block"]').click()
drive.find_element_by_xpath('//*[@id="aside"]/div/div/nav/ul/li[8]/a/span').click()
drive.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/table/tbody/tr/td[6]/div/a[1]').click()
drive.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/section/div/div/div[3]/div/div/div/table/thead/tr[13]/td').click()

time.sleep(5)
