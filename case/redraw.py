#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
import json

from iphoneinfo import shoujiinfo
device=shoujiinfo.connnect_ipad_device()
import time
import requests
def getsize():
	'''
	获得手机屏幕大小
	:param device: 测试的手机
	:return: 手机屏幕大小
	'''
	x = device.get_window_size()['width']
	y = device.get_window_size()['height']
	return x,y


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
u'积分商城'
def faxian_all():
	# '''
	# 点击积分商场的兑换记录
	# :return:
	# '''
	device.implicitly_wait(30)
	device.find_elements_by_class_name ('android.widget.RadioButton') [2].click ()
	# #device.find_elements_by_class_name('android.widget.ImageView')[0].click()
	# u'平台数据'
	# device.find_elements_by_class_name('android.widget.TextView')[0].click()
	# swipe_to_up(1000)
	# time.sleep(2)
	# device.back()
	# u'安全保障'
	# device.find_elements_by_class_name ('android.widget.TextView') [1].click ()
	# for i in range(6):
	# 	for a in range(2):
	# 		device.find_elements_by_class_name('android.widget.Image')[1+i].click()
	# device.back()
	# u'查看积分'
	# device.find_element_by_id('com.yourenkeji.shenghuidai:id/jifenshangcheng').click()
	# device.find_elements_by_class_name('android.widget.Image')[0].click()
	# device.back()
	# for i in range(8):
	# 	if i >= 5:
	# 		swipe_to_up(1000)
	# 		device.find_elements_by_class_name('android.widget.Image')[2+i].click()
	# 		time.sleep(2)
	# 		device.back()
	# 	else:
	# 		device.find_elements_by_class_name ('android.widget.Image') [2 + i].click ()
	# 		time.sleep(2)
	# 		device.back()
	# device.back()
	# u'活动中心'
	# device.find_element_by_id('com.yourenkeji.shenghuidai:id/huodongzhongxin').click()
	# device.back()
	u'发现更多'

	url = "https://api.shenghuidai.com:8012/v1/news/media/all"

	headers = {'Cache-Control': "no-cache", 'Postman-Token': "3949fa4d-8390-539d-dee7-a28c5565b02a"}

	response = requests.request ("POST", url, headers = headers)
	response = json.loads (response.text)
	xinwen_geshu=[]
	if response ['code'] == str (10000):
		print ("请求接口数据成功")
		xinwen_geshu = []
		for i in response ['content']:
			xinwen_geshu.append (len (i))
	else:
		print ("失败喽")
	print(f'一共有{len(xinwen_geshu)}条新闻,前6条显示就可以默认都显示正常了')
	xinwen_shuliang=int(len(xinwen_geshu))
	device.find_elements_by_class_name ('android.widget.TextView') [6].click ()
	for i in range(xinwen_shuliang):
		if i <=6:
			device.find_elements_by_class_name('android.widget.ImageView')[i+1].click()
			time.sleep(2)
			swipe_to_up(1000)
			device.back()
		else:
			pass
def toubiao():
	u'投标'
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
def gonggao():

	device.implicitly_wait(10)
	device.find_elements_by_class_name('android.widget.LinearLayout')[10].click()


if __name__ == '__main__':
	time.sleep(10)
	faxian_all()