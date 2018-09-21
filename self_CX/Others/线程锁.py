#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"
# import threading
# import time
#
#
# def run(n):
# 	global a
# 	print('runing :',n)
# 	time.sleep(2)
# 	a+=1
#
# a=1
# b=[]
# for i in range(100):
# 	t=threading.Thread(target = run,args = (i,))
# 	t.setDaemon(True)#守护线程
# 	t.start()#
# 	b.append(t)
#
# # for n in b:
# # 	n.join()    #等待线程
#
# print('主线程',threading.current_thread())

# print('\033[43;3m 嗯嗯 \033[0m')
"""
汽车等待红绿灯

"""
import threading

event = threading.Event ()
event.set ()


def deng ():
	count = 0
	while True:
		if 5 < count < 10:
			event.clear ()
			print ('现在红灯不可以通行请等待')
		elif count > 10:
			event.set ()
			count = 0
		else:
			print ('现在是绿灯请前进')
		time.sleep (1)
		count += 1


def car (name):
	while True:
		if event.is_set ():
			print ('%s车子正在通行中' % name)
			time.sleep (1)
		else:
			print ('红灯请等待')
			event.wait ()


deng1 = threading.Thread (target = deng)
deng1.start ()
car1 = threading.Thread (target = car, args = ('奔驰600',))
car1.start ()

import queue, time
import threading

a = queue.Queue (maxsize = 10)


def Shengchan (aa):
	b = 1
	while True:
		a.put (b)
		print (aa, '正在生产')
		time.sleep (10)
		b += 1
		print ('\n')


def eat (name):
	while True:
		a.get ()
		print ('正在吃', name)


c = threading.Thread (target = Shengchan, args = ('大熊猫',))
c.start ()
c1 = threading.Thread (target = eat, args = ('panda',))
c1.start ()
c2 = threading.Thread (target = eat, args = ('damao',))
c2.start ()
