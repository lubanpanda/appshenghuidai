#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import os

from selenium import webdriver
from selenium.webdriver.support.select import Select


class signAndClock(object):
    def __init__(self):
        self.inputInfoMap = {
            "workID": 19042501,
            "Name": "于成涛",
            "City": '上海',
            "morningTemperature": 1,
            "aftrtnoonTemperature": 1,
            "health": "健康",
            "isGeli": "小区隔离",
            "things": "远程办公",
            "Workbatches": "其他",
            "projectID": "P18040002"
        }
        self.driver = webdriver.Chrome("/Users/panda/Downloads/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def h5Sign(self):
        self.driver.get("https://erp.fulan.com.cn/wendu/wendu.html")
        self.driver.find_element_by_id("q1").send_keys(self.inputInfoMap.get("workID"))
        self.driver.find_element_by_id("q7").send_keys(self.inputInfoMap.get("Name"))
        self.driver.find_element_by_id("q4").send_keys(self.inputInfoMap.get("City"))
        self.driver.find_element_by_id("q9").send_keys(self.inputInfoMap.get("projectID"))
        self.driver.find_element_by_xpath('//*[@id="div32"]/div[2]/div[1]/div').click()
        self.driver.find_element_by_xpath('//*[@id="div33"]/div[2]/div[1]/div').click()
        S1 = Select(self.driver.find_element_by_id("q5"))
        S1.select_by_value(self.inputInfoMap.get("things"))
        S2 = Select(self.driver.find_element_by_id("q13"))
        S2.select_by_value("4")
        S3 = Select(self.driver.find_element_by_id("q14"))
        S3.select_by_value("9")


if __name__ == '__main__':
    a = signAndClock()
    a.h5Sign()
    os.popen("packaging.py")
