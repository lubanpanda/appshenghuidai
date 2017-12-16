#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  84305510@qq.com

import time,os
timestamp = time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime ())
print(timestamp)

adb_device = os.popen("adb shell pm list packages -3").readlines()
print(adb_device)