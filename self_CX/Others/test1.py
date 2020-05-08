#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

#
# from collections import deque, defaultdict
#
# p=(4,5)
# x,y=p
# # print(x)
#
# q=deque()
# q.append(1)
# q.append(2)
# q.append(3)
# q.appendleft(4)
# print(q)
# d=defaultdict(set)
# d['a'].add(1)
# d['a'].add(2)
# d['b'].add(4)
# print(d)
# import re
# re.split()
from appium import webdriver

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', "desired_caps")

import time


def times(func):
    def addtime(string):
        start = time.time()
        func(string)
        stop = time.time()
        huafeitime = stop - start
        print(f"这是一个参数string的输出内容{string}")
        print(f"一共花费{huafeitime}秒了")

    return addtime


@times
def runtime(sss):
    """
    文档说明
    :param sss:hahaha
    :return:
    """
    time.sleep(1)
    print(sss)


class logger(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("[{level}]: the function {func}() is running...".format(level=self.level, func=func.__name__))
            func(*args, **kwargs)

        return wrapper


@logger(level="WARNING")
def say(something):
    print("say {}!".format(something))


say("hello")
