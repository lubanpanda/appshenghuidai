#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda

from iphoneinfo import shoujiinfo
device=shoujiinfo.connnect_ipad_device()
import time
def getsize():
	'''
	获得手机屏幕大小
	:param device: 测试的手机
	:return: 手机屏幕大小
	'''
	x = device.get_window_size()['width']
	y = device.get_window_size()['height']
	return x, y


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

def toubiao():
	time.sleep(8)
	device.find_elements_by_class_name('android.widget.RelativeLayout')[1].click()
	jine=device.find_elements_by_class_name('android.widget.EditText')[0]
	device.set_value(jine,10000)
	device.find_elements_by_class_name('android.widget.Button')[1].click()
	device.find_elements_by_class_name('android.widget.Button')[0].click()
	for i in range (6):
		password = device.find_elements_by_class_name ('android.widget.Button')[0]
		password.click()
	shouye_to=device.find_elements_by_class_name('android.widget.RadioButton')
	time.sleep(5)
	if shouye_to and len(shouye_to)==0:
		a=shouye_to[0]
		print(a,'密码正确')
	else:
		print('密码错误,正在尝试第二种密码......')
		device.find_elements_by_class_name ('android.widget.Button') [0].click ()
		for i in range(6):
			new_password=device.find_elements_by_class_name('android.widget.Button')[i]
			new_password.click()
		print("密码正确，交易成功")
		device.find_elements_by_class_name('android.widget.Button')[0].click()


if __name__ == '__main__':

	time.sleep(8)
	swipe_to_up(1000)
	toubiao()
