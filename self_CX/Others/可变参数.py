#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/5/9 09:59
"""
可变参数的用法
"""


class argdemo (object):
	def __init__ (self, name):
		self.name = name

	def printdif (self, name, key = None, *args, **kwargs):
		self.name = name
		print (self.name)
		print (key)
		print ("args=======%s" % str (args))
		count = 0
		for value in args:
			count += 1
			print ("args's No.%s value:%s" % (count, value))
			print ("kwargs=======%s" % str (kwargs))
		for key in kwargs:
			print ("**kwargs's key=%s,value=%s" % (key, kwargs [key]))


if __name__ == '__main__':
	arg = argdemo ("name1")
	print (arg.name)
	arg.printdif ("name2", "B", ["C", "D"], {"key1": "E"}, key1 = "hello", key2 = "world")
