#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
import datetime
def zhuangshi(fune):
	def zhuang():
		star=datetime.datetime.now()
		fune()
		stop=datetime.datetime.now()
		print('花费时间为：',stop-star)
	return zhuang
@zhuangshi
def cesi():
	print('wolaile')
	a=datetime.datetime.now()
	print(a)


def deco (func):
	def _deco (a, b):
		print ("before myfunc() called.")
		ret = func (a, b)
		print ("  after myfunc() called. result: %s" % ret)
		return ret

	return _deco


@deco
def myfunc (a, b):
	print (" myfunc(%s,%s) called." % (a, b))
	return a + b


myfunc (1, 2)
myfunc (3, 4)
