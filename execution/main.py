#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
from appium import webdriver
import os
import time
def connnect_ipad_device():
	'''
	定义测试平台的属性
	:return: device及参数
	'''
	try:

		import time
		desired_caps = {
			'platformName': 'Android',
			'deviceName': '3cdbb8e5',
			'platformVersion': '7.0',
			'sessionOverride': True,
			'appPackage': 'com.yourenkeji.shenghuidai',
			'newCommandTimeout': 600,
			'appActivity': 'com.delevin.shenghuidai.welcome.WelcomeActivity',
			'autoAcceptAlerts': True,
			'noReset':True,   #不要在会话前重置应用状态。默认值false
			'unicodeKeyboard':True,#设置appium输入法后就不会弹默认的系统输入法了
			'resetKeyboard':False, #重置系统输入法

		}
		driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		return driver
	except Exception as e:
		print(e)


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
	photo=os.popen ("adb pull /data/local/tmp/tmp.png " + PATH (path + "/" + name+timestamp + ".png"))
	os.popen ("adb shell rm /data/local/tmp/tmp.png")
	print('success,已经成功的保存在当前目录下')


def ture_or_flase():
	'''
	判断是否登录
	:return:
	'''
	try:
		a=device.find_elements_by_class_name ('android.widget.TextView') [14]
		return True
	except Exception :
		return False
def login():

	# 等待启动，设置程序休眠/防止手机反应慢卡死
	time.sleep(5)
	#点击账户
	device.find_elements_by_class_name ('android.widget.RadioButton') [3].click ()

	#点击更多
	if ture_or_flase() is True:
		print('准备开始切换账户了')
		device.find_elements_by_class_name ('android.widget.TextView') [14].click()
		device.find_elements_by_class_name('android.widget.Button')[0].click()
		#确定

		device.find_elements_by_class_name('android.widget.Button')[0].click()
		# 点击账户
		device.find_elements_by_class_name ('android.widget.RadioButton') [3].click ()
		#登录
		device.find_elements_by_class_name('android.view.View')[6].click()
		#登录账户
		device.find_elements_by_class_name ('android.widget.EditText') [0].clear()
		login_ip=device.find_elements_by_class_name('android.widget.EditText')[0]
		device.set_value(login_ip,'18519291259')
		device.find_elements_by_class_name('android.widget.Button')[0].click()
		#密码
		password=device.find_elements_by_class_name('android.widget.EditText')[0]
		device.set_value(password,'111111')
		device.find_elements_by_class_name('android.widget.Button')[0].click()
		#跳过手势密码
		device.find_elements_by_class_name ('android.widget.ImageView') [9].click ()
	else:
		print("准备开始登录了")
		# 登录
		device.find_elements_by_class_name ('android.view.View') [6].click ()
		# 登录账户
		device.find_elements_by_class_name ('android.widget.EditText') [0].clear ()
		login_ip = device.find_elements_by_class_name ('android.widget.EditText') [0]
		device.set_value (login_ip, '18519291259')
		device.find_elements_by_class_name ('android.widget.Button') [0].click ()
		# 密码
		password = device.find_elements_by_class_name ('android.widget.EditText') [0]
		device.set_value (password, '111111')
		device.find_elements_by_class_name ('android.widget.Button') [0].click ()
		# 跳过手势密码
		device.find_elements_by_class_name ('android.widget.ImageView') [9].click ()


def toubiao():

	time.sleep(8)
	device.find_elements_by_class_name('android.widget.RelativeLayout')[1].click()
	jine=device.find_elements_by_class_name('android.widget.EditText')[0]
	device.set_value(jine,1000)
	device.find_elements_by_class_name('android.widget.Button')[1].click()
	device.find_elements_by_class_name('android.widget.Button')[0].click()
	for i in range (6):
		new_password = device.find_elements_by_class_name ('android.widget.Button') [i]
		new_password.click ()

	shouye_to=device.find_elements_by_class_name('android.widget.RadioButton')
	time.sleep(5)
	if shouye_to and len(shouye_to)==0:
		a=shouye_to[0]
		print(a,'密码正确')
	else:
		print('密码错误,正在尝试第二种密码......')
		device.find_elements_by_class_name ('android.widget.Button') [0].click ()
		for i in range (6):
			password = device.find_elements_by_class_name ('android.widget.Button') [0]
			password.click ()
		print("密码正确，交易成功")
		device.find_elements_by_class_name('android.widget.Button')[0].click()
if __name__ == '__main__':
    device=connnect_ipad_device()
    time.sleep(8)
    swipe_to_up (1000)
    toubiao()