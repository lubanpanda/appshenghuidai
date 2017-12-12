#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/6/19 下午9:46
# @Author  : Panda

import sys,time

count = 0
while count < 10:
    ncount = 10 - count
    sys.stdout.write("\r%d " % ncount)
    sys.stdout.flush()
    time.sleep(1)
    count += 1