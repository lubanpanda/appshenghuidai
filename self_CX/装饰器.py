#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/5/2 14:35

import time

def timer(fun):
    def deco(*args, **kwargs):
        start = time.time()
        fun(*args, **kwargs)
        stop = time.time()
        print(stop-start)
    return deco

@timer
def test(name):
    time.sleep(2)
    print("%s test is running!"%name)
test('panda')


