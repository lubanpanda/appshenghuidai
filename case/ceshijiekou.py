#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  84305510@qq.com
import os,time

# os.popen('adb shell input keyevent 26')
# time.sleep(1)
# os.popen('adb shell input swipe 50 1000 50 0 100')
b=''
def d():

	b=os.popen('adb shell dumpsys window policy|grep mScreenOnFully')
	a=b.read().strip()
	deng=a[-5:]
	if deng==str('false'):
		print('屏幕是灭的,等待解锁')
		os.popen('adb shell input keyevent 26')
		time.sleep(1)
		os.popen('adb shell input swipe 50 1000 50 0 100')
	else:
		print('不是锁屏状态,可直接执行项目哦')



if __name__ == '__main__':
    d()