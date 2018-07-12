#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import os

backmag = input ('请输入包名' + os.linesep)
buidls = input ('请输入版本号,没有版本号输入1')
if buidls == str (1):
	print (os.system (f"pip3 install {backmag}"))
else:
	print (os.system (f"pip3 install {backmag}=={buidls}"))
