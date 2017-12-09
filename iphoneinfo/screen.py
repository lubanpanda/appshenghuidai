#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
import os
import time

PATH = lambda p: os.path.abspath (p)


def screenshot (name):
	'''
	截取手机屏幕
	:param name:相片文件名
	:return:
	'''
	path = PATH (os.getcwd () + "/screenshot")
	timestamp = time.strftime ('%Y-%m-%d-%H-%M-%S', time.localtime (time.time ()))
	os.popen ("adb wait-for-device")
	os.popen ("adb shell screencap -p /data/local/tmp/tmp.png")
	if not os.path.isdir (PATH (os.getcwd () + "/screenshot")):
		os.makedirs (path)
	os.popen ("adb pull /data/local/tmp/tmp.png " + PATH (path + "/" + name+timestamp + ".png"))
	os.popen ("adb shell rm /data/local/tmp/tmp.png")
	print('success,已经成功的保存在当前目录下')


if __name__ == "__main__":
	screenshot ('胜辉贷')