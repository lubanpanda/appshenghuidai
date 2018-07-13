#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/3/3 21:05
import os
import re

import requests


def Climb_the_pictures ():
	UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
	url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%C3%C0%C5%AE%CD%BC%C6%AC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111'
	url_info = requests.get (url, headers = {'User-Agent': UA})
	ptoho = url_info.text
	a = re.compile ("https.*?\.jpg")
	b = re.findall (a, ptoho)
	a = os.path.exists ('panda')
	a if a else os.mkdir ('panda')
	q = 1
	url_adds = []
	url_add = []
	for i in b:
		if i.endswith ('jpg'):
			url_adds.append (i)
	for i in url_adds:
		if i in url_add:
			continue
		else:
			url_add.append (i)
	for a in url_add:
		c = requests.get (a)
		with open ('../Others/panda/' + str (q) + '.png', 'wb') as f:
			f.write (c.content)
		print (f'正在下载第{q}张图片')
		q += 1


if __name__ == '__main__':
	Climb_the_pictures ()
