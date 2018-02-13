#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2017/12/31 20:15
# @File : zhengze.py
# @Software: PyCharm

import re
import random
# a="嗯那12321421 你好大额啊让我请让我去"
#
# b=re.findall('[\u4e00-\u9fa5]+',a)
# print(b)
#
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.findall('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(result)
class tese_zz():
	def tese_01(self):
		a='积分 340952'

		w=re.findall('[A-Za-z0-9]+',a)
		print(w)
a=tese_zz()
a.tese_01()
suiji_list_to = random.randrange (7, 28, 3)
print(suiji_list_to)


f=open('QQ.text','r')
f1=open('q.text','w')
b=f.readlines()
for i in b:
	w=i.replace('你','hello')
	f1.write(w)
f1.write(i)
f.close()
f1.close()