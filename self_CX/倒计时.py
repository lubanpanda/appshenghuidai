#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/6/19 下午9:46
# @Author  : Panda
import os
a=os.listdir()
for i in a:
    print(i)
#
# for (dirpath, dirnames, filenames) in os.walk ('./'):  # 第一个起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。
#     for file in filenames:
#         print(file)
# import sys,time
#
# count = 0
# while count < 10:
#     ncount = 10 - count
#     sys.stdout.write("\r%d " % ncount)
#     sys.stdout.flush()
#     time.sleep(1)
#     count += 1