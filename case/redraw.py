#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
import time

from iphoneinfo import shoujiinfo
device=shoujiinfo.connnect_ipad_device()

def getsize():
	'''
	获得手机屏幕大小
	:param device: 测试的手机
	:return: 手机屏幕大小
	'''
	x = device.get_window_size()['width']
	y = device.get_window_size()['height']
	return (x, y)


def swipe_to_up(duration):
	'''
	屏幕向上滑动
	:param duration: 滑动的毫秒数值
	:return:
	'''
	screen_size = getsize()
	# X坐标
	x1 = int(screen_size[0] * 0.5)
	# 起始Y坐标
	y1 = int(screen_size[1] * 0.75)
	# 终点Y坐标
	y2 = int(screen_size[1] * 0.25)
	device.swipe(x1, y1, x1, y2, duration)


def swipe_to_down(duration):
	'''
	屏幕向下滑动
	:param duration: 滑动的毫秒数值
	:return:
	'''

	screen_size = getsize()
	x1 = int(screen_size[0] * 0.5)
	y1 = int(screen_size[1] * 0.25)
	y2 = int(screen_size[1] * 0.75)
	device.swipe(x1, y1, x1, y2, duration)


def swipe_to_left(duration):
	'''
	屏幕向左滑动
	:param duration: 滑动持续的毫秒值
	:return:
	'''

	device.find_elements_by_class_name ('android.widget.RadioButton') [2].click ()
	screen_size = getsize()
	x1 = int(screen_size[0] * 0.75)
	y1 = int(screen_size[1] * 0.5)
	x2 = int(screen_size[0] * 0.05)
	device.swipe(x1, y1, x2, y1, duration)


def swipe_to_right(duration):
	'''
	屏幕向右滑动
	:return:
	'''
	screen_size = getsize()
	x1 = int(screen_size[0] * 0.05)
	y1 = int(screen_size[1] * 0.5)
	x2 = int(screen_size[0] * 0.75)
	device.swipe(x1, y1, x2, y1, duration)




time.sleep(5)

swipe_to_left(1000)
time.sleep(2)
swipe_to_right(1000)
time.sleep(2)
swipe_to_down(1000)