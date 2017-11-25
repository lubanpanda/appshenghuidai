#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
from case import login
import time
from case import Homepage
from case import redraw

if __name__ == '__main__':
    time.sleep(5)
    now_time = time.strftime ("%Y-%m-%d %H:%M:%S", time.localtime ())
    login.login()
    # time.sleep(5)
    # redraw.swipe_to_up(1000)
    # time.sleep(2)
    # Homepage.toubiao()
    print(now_time)