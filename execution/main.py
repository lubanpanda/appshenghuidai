#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
from case import login
import time

if __name__ == '__main__':
    now_time = time.strftime ("%Y-%m-%d %H:%M:%S", time.localtime ())
    login.login()
    print(now_time)