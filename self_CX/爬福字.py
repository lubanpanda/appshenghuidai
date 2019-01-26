#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import os
import re
import requests

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%B8%A3%D7%D6%CD%BC%C6%AC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111'
c = requests.get(url=url, headers={'User-Agent': UA})
aa = c.text
a = re.compile("https.*?\.jpg")
b = re.findall(a, aa)
print(b)
q = 1
e = os.path.exists('fu')
e if e else os.mkdir('fu')
for i in b:
    c = requests.get(i)
    with open(os.path.abspath(os.curdir) + '/Others/' + 'fu/' + str(q) + '.jpg', 'wb') as f:
        f.write(c.content)
        print(f'正在下载第{q}张图片')
        q += 1
