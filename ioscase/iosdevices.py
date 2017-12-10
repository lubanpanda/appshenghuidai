#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  84305510@qq.com
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def ios_devices():
	chrom=webdriver.Chrome('/Users/yuchengtao/node_modules/accepts/chromedriver')
	chrom.get("https://www.baidu.com/")
	chrom.implicitly_wait(70)
	chrom.find_element_by_xpath('//*[@id="kw"]').send_keys(u'随便点吧')
	time.sleep(20)

if __name__ == '__main__':
    ios_devices()