#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2017/12/31 20:15
# @File : zhengze.py
# @Software: PyCharm

import re

a="嗯那12321421 你好大额啊让我请让我去"

b=re.findall('[\u4e00-\u9fa5]+',a)
print(b)

content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.findall('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)