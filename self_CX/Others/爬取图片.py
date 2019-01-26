#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/3/3 21:05
import os
import re

import requests


def Climb_the_pictures():
    url = input('请输入百度网址的图片网址')
    UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    # url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%B8%A3%D7%D6%CD%BC%C6%AC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111'
    url_info = requests.get(url, headers={'User-Agent': UA})
    ptoho = url_info.text
    a = re.compile("https.*?\.jpg")
    b = re.findall(a, ptoho)
    a = os.path.exists('panda')
    a if a else os.mkdir('panda')
    q = 1
    url_adds = []
    url_add = []
    for i in b:
        if i.endswith('jpg'):
            url_adds.append(i)
    for i in url_adds:
        if i in url_add:
            continue
        else:
            url_add.append(i)
    for a in url_add:
        c = requests.get(a)
        with open(os.path.abspath(os.curdir) + os.sep + 'panda' + os.sep + str(q) + '.png', 'wb') as f:
            f.write(c.content)
        print(f'正在下载第{q}张图片')
        q += 1


if __name__ == '__main__':
    Climb_the_pictures()
