#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import requests
import urllib3
import xlwt
from bs4 import BeautifulSoup
from selenium import webdriver

"""
重庆菜会卡一下，得手动返回一下
"""

urllib3.disable_warnings()
url = 'http://www.chaxuntu.com/caipu/'


class Crecipe(object):
    def __init__(self):
        self.i = 1
        self.ii = 1
        self.CAI_PU_INFO = {}
        self.recipe_id = []
        self.book = xlwt.Workbook(encoding='utf-8')  # style_compression是否进行文件压缩，0代表否
        self.sheet = self.book.add_sheet('菜谱', cell_overwrite_ok=True)
        self.derive = webdriver.Chrome(
            '/Applications/Appium.app/Contents/Resources/app/node_modules/appium-chromedriver/chromedriver/mac/chromedriver')
        self.derive.implicitly_wait(30)

    def menu_url(self):
        pp = requests.get(url)
        caipu_txt = pp.text
        jie_xi_txt = BeautifulSoup(caipu_txt, 'html.parser')
        Quan = jie_xi_txt.find(name='div', class_='mcon center miniMenu')
        for i in Quan.find_all():
            self.CAI_PU_INFO[i.string] = url + i.get('href')
            self.recipe_id.append(i.string)

    def menu_info(self):
        for i in self.recipe_id[0:11]:
            url = self.CAI_PU_INFO.get(i)
            self.derive.get(url)
            for i in range(10):
                while 1:
                    try:
                        self.derive.find_element_by_xpath(
                            f"/html/body/div[2]/div[1]/div[2]/div[5]/table/tbody/tr[{i+1}]/td[2]/div[2]/a").click()
                        aaa = True

                        break
                    except:
                        continue
                if aaa:
                    name = self.derive.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[2]/h2').text  # 名字
                    peiliao = self.derive.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[2]').text  # 配料
                    zuofa = self.derive.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[4]/p[1]').text  # 做法
                    self.excel(self, name, zuofa)
                    self.derive.back()

    def excel(self, name, zuofa, peiliao):
        self.sheet.write(self.i, 0, name)
        self.sheet.write(self.ii, 1, peiliao)
        self.sheet.write(self.ii, 2, zuofa)
        self.i += 1
        self.ii += 1
        self.book.save('菜谱.xls')

    def main(self):
        a = Crecipe()
        a.menu_url()
        a.menu_info()
        self.derive.quit()


if __name__ == '__main__':
    Crecipe().main()
