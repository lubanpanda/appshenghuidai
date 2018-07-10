#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
import os

for (dirpath, dirnames, filenames) in os.walk ('./'):  # 第一个起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。
	for file in filenames:
		print(file)