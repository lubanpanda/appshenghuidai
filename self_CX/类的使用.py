#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2017/12/31 17:42
# @File : 类的使用.py
# @Software: PyCharm
class People(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def play(self):
		print('%s 正在玩..........'%self.name)

	def eat(self):
		print ('%s 正在吃..........' % self.name)


class life(object):
	def good_life(self,obj,lin):
		print('%s 正在吃饺子，%s吃的是寿司，%s上班睡过了'%(self.name,obj.name,lin.name))


class man(People,life):
	def __init__(self,name,age,xingbie):
		super(man,self).__init__(name,age)
		self.xingbie=xingbie
	def working(self):
		print('%s 正在工作,他是%s'%(self.name,self.xingbie))
	def eat(self):
		super().eat()
		print('%s 也在吃'%self.name)
m1=man('panda',24,'男')
m2=man('wangmin',22,'女')
# m1.working()
m1.eat()
#m1.good_life(m2,m2)