#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import unittest

from selenium import webdriver

CHAROM = "/Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac/chromedriver"


class Case(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.URL = "https://consumer.huawei.com/cn/"
        self.driver = webdriver.Chrome(
            "/Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac/chromedriver")
        self.driver.implicitly_wait(70)
        self.driver.get(self.URL)

    @classmethod
    def tearDownClass(self) -> None:
        print('用例执行完毕，详细结果请看测试报告')
        self.driver.quit()

    def test_case01(self):
        self.driver.maximize_window()
        phone = self.driver.find_element_by_xpath("//*[@id='header-v3']/div[2]/div[2]/div[1]/ul/li[1]/a").text
        print(phone)


driver = webdriver.Chrome(CHAROM)
driver.get("https://www.vmall.com/")

driver.find_element_by_xpath("//a[@href='http://consumer.huawei.com/cn/']").click()
driver.implicitly_wait(120)
current_handle = driver.current_window_handle  # 当前窗口
handles = driver.window_handles
for handle in handles:
    if handle != current_handle:
        driver.switch_to.window(handle)
        menus = driver.find_elements_by_css_selector(".products-name")
        # print(menus)
        for menu in menus:
            print(menu.text + "111")
# print(menu_text)


# if __name__ == '__main__':
#     unittest.main()
# suite = unittest.TestSuite()
# suite.addTest(Case('test_case01'))
# loca_file = os.getcwd()
# report_file = loca_file + "case.html"
# fp = open(report_file, 'wb')
# baogao_info = '测试报告'
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="接口测试报告", description=baogao_info)
# runner.run(suite)
# fp.close()
