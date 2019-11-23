#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


# 基于原生的selenium做二次封装
class Base():
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10  # 最长超时时长
        self.t = 0.5  # 查询元素的间隔时间

    # 定位元素：定位到元素，返回元素对象，没定位到，TimeOut异常
    def find_element(self, locator):
        if not isinstance(locator, tuple):  # 检查传的参数是否为元组类型
            print('locator参数类型错误，必须传元组类型：loc=("id","value")')
        else:
            print("正在定位元素信息:定位方式->%s,Value值->%s" % (locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            return ele

    # 定位一组元素：定位到元素，返回元素列表，没定位到，返回空列表
    def find_elements(self, locator):
        if not isinstance(locator, tuple):  # 检查传的参数是否为元组类型
            print('locator参数类型错误，必须传元组类型：loc=("id","value")')
        try:
            print("正在定位元素信息：定位方式->%s，value值->%s" % (locator[0], locator[1]))
            eles = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_all_elements_located(locator))
            return eles
        except:
            return []

    # 文本框赋值
    def send_keys(self, locator, text=""):
        ele = self.findElement(locator)
        ele.send_keys(text)

    def click(self, locator):
        ele = self.findElement(locator)
        ele.click()

    def clear(self, locator):
        ele = self.findElement(locator)
        ele.clear()

    # 判断元素是否被选中，返回bool值
    def is_selected(self, locator):
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    # 判断元素是否存在，返回bool值
    def is_element_xist(self, locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False

    # 判断标题是否与预期结果一致，返回bool值
    def is_title(self, title=''):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
            return result
        except:
            return False

    # 判断标题是否包含预期内容，返回bool值
    def is_title_ontains(self, title=''):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
            return result
        except:
            return False

    # 判断指定元素中是否包含预期字符串，返回bool值
    def is_text_in_element(self, locator, text=''):
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value")')
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    # 判断指定元素的value属性值中包含预期字符串，返回bool值
    def is_value_in_element(self, locator, value=''):
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value")')
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False

    # 判断页面上是否有alert，返回bool值
    def is_alert(self, timeout=3):
        try:
            result = WebDriverWait(self.driver, timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    # 切换到alert并返回alert的内容
    def switch_alert(self):
        r = self.is_alert()
        if not r:
            print("alert不存在")
        else:
            return r

    # 获取title值
    def get_title(self):
        return self.driver.title

    # 获取文本
    def get_text(self, locator):
        try:
            text = self.find_element().text
            return text
        except:
            print('获取text失败，返回""')
            return ""

    # 获取属性
    def get_attribute(self, locator, attribute_name):
        try:
            elem = self.find_element(locator)
            return elem.get_attribute(attribute_name)
        except:
            print('获取%s失败，返回""' % attribute_name)
            return ""

    # 聚焦元素
    def js_focus_element(self, locator):
        target = self.find_element(locator)
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, target)

    # 滚动到顶部
    def js_scroll_top(self):
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    # 滚动到底部
    def js_scroll_bottom(self, x=0):
        js = "window.scrollTo(%s,document.body.scrollHeight)" % x
        self.driver.execute_script(js)

    # 根据索引选择下拉框选项,默认选第1个
    def select_by_index(self, locator, index=0):
        ele = self.find_element(locator)  # 定位select这一栏
        Select(ele).select_by_index(index)

    # 根据value属性定位下拉框选项
    def select_by_value(self, locator, value):
        ele = self.find_element(locator)  # 定位select这一栏
        Select(ele).select_by_value(value)

    # 根据文本值定位下拉框选项
    def select_by_text(self, locator, text):
        ele = self.find_element(locator)  # 定位select这一栏
        Select(ele).select_by_visible_text(text)

    # 切换iframe
    def switch_to_frame(self, id_index_locator):
        try:
            # 用index定位
            if isinstance(id_index_locator, int):
                self.driver.switch_to.frame(id_index_locator)
            # 用id/name定位
            elif isinstance(id_index_locator, str):
                self.driver.switch_to.frame(id_index_locator)
            # 用find_element系列方法取得WebElement对象
            elif isinstance(id_index_locator, tuple):
                ele = self.find_element(id_index_locator)
                self.driver.switch_to.frame(ele)
        except:
            print("iframe切换异常")

    # 切换到指定的window_name页面，window_name:指定页面窗口的handle
    def switch_window(self, window_name):
        self.driver.switch_to.window(window_name)

    # 鼠标悬停操作
    def move_to_element(self, locator):
        ele = self.find_element(locator)
        ActionChains(self.driver).move_to_element(ele).perform()


if __name__ == '__main__':
    driver = webdriver.Chrome(r"D:\chromedriver.exe")
    web = Base(driver)
