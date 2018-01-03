#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  84305510@qq.com
import random
import time
import os
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from SHD_automation.panda_log.log import *
from SHD_automation.device_info.device import *

class My_method(object):
	'获取ID元素'
	def My_id(self,id,text,sleep_time=0):
		if text == '获取元素':
			pro = '获取元素：'
			logging.info (u'>>>%s%s' % (pro, id))
			return self.driver.find_element_by_id (id),time.sleep(sleep_time)
		else:
			if text == 'click':
				pro = '点击控件获取'
				logging.info (u'>>>%s%s' % (pro, id))
				return self.driver.find_element_by_id (id).click (),time.sleep(sleep_time)
			elif text=='获取内容':
				pro='获取控件里的text内容'
				logging.info('>>>%s%s'%(pro,id))
				return self.driver.find_element_by_id(id).text,time.sleep(sleep_time)

			else:
				pro = '输入内容为：'
				logging.info (u'>>>定位控件%s,%s%s' % (id, pro, text))
				return self.driver.find_element_by_id (id).set_text (text),time.sleep(sleep_time)


	'''方法包装_通过当前页面:classname+text定位控件并完成输入'''
	def my_class_name_shuru (self,className, text, txtUsername):
		allClassNames = self.driver.find_elements_by_class_name (className)  # 定义所有该className下所有控件为 allclassname
		for allClassName in allClassNames:
			print (allClassName.text)
			if text in allClassName.text:  # 当text的值属于  遍历出来当中的一个text值时，则为我们需要的值
				allClassName.set_text (txtUsername)
				break

	'''封装一个根据clsaa+id的方法点击控件'''
	def my_class_name_id_dianji(self,classname,list_id,text,sleep_time=0):

		if text == '获取元素':
			pro = '获取classname元素：'
			logging.info (u'>>>%s%s' % (pro, classname))
			return self.driver.find_elements_by_class_name(classname)
		else:
			if text == 'click':
				pro = '点击控件classname：'
				logging.info (u'>>>%s%s索引数字：%s' % (pro, classname,list_id))
				return self.driver.find_elements_by_class_name(classname)[list_id].click (),time.sleep(sleep_time)
			else:
				pro = '输入内容为：'
				logging.info (u'>>>定位控件%s,%s%s' % (classname, pro, text))
				return self.driver.find_element_by_id (classname).set_text (text)
	'''封装一个根据clsaa+text的方法点击控件 '''
	def my_class_name_shuru_dianji (self, className, text):
		clickClassName = self.driver.find_elements_by_class_name (className)
		for clickclassNameOne in clickClassName:
			if text in clickclassNameOne.text:
				clickclassNameOne.click ()
				break

	'''封装一个根据class+text的方法获取元素'''
	def my_classText_huoqu (self, className, text):
		clickClassName = self.driver.find_elements_by_class_name (className)
		for clickclassNameOne in clickClassName:
			if text in clickclassNameOne.text:
				print (text)
				print (clickclassNameOne)
				logging.info (text)
				break
			else:
				logging.info ('sjoj')

	'''封装一个获取className的方法（className唯一）'''
	def huoQu_className (self, className):

		return self.driver.find_element_by_class_name (className)

	'''封装一个滑动当前页面查找元素方法'''
	def scroll_resourceId (self, driver, classNameCode, textCode):
		driver.find_element_by_android_uiautomator (
			'new UiScrollable(new UiSelector().resourceId("%s")).scrollIntoView(new UiSelector().text("%s"))' % (
				classNameCode, textCode))

	'''封装一个滑动当前页面class+text查看元素方法'''

	def scroll_classText (self, classNameCode, textCode):
		self.driver.find_element_by_android_uiautomator (('new UiScrollable(new UiSelector().className("%s")).scrollIntoView(new UiSelector().text("%s"))' % (classNameCode, textCode)))

	'''封装退出APP方法'''

	def back_Login (self):
		time.sleep (10)
		self.driver.find_element_by_id (module_info['账户']).click ()
		os.popen ('adb shell input swipe 50 1000 50 0 100')
		self.driver.find_element_by_id (account['更多']).click ()
		self.driver.find_element_by_id (module_info['退出']).click ()
		self.driver.find_element_by_id ('com.yourenkeji.shenghuidai:id/positiveButton').click ()
	'''封装获取toast方法'''
	def find_toast (self,message):

		toast_Code = ('xpath', './/*[contains(@text,"%s")]' % message)
		t = WebDriverWait (self.driver, 5,0.1).until (EC.presence_of_element_located (toast_Code))
		logging.info(f'获取到toast:{t}')



	'''封装登陆方法'''
	def loginCode (self,username,password):
		# 登录
		My_method.My_id (self, module_info ['账户'], 'click')
		My_method.My_id (self, zhuce ['登录'], 'click')
		My_method.My_id (self, zhuce ['账号'], username)
		My_method.My_id (self, 'com.yourenkeji.shenghuidai:id/zhu_bt', 'click')
		My_method.My_id (self, zhuce ['密码'], password)
		My_method.My_id (self, 'com.yourenkeji.shenghuidai:id/denglu_bt_a', 'click')
		My_method.My_id (self, zhuce ['跳过'], 'click')
		logging.info ('初始化登陆成功')

	'''封装一个退出方法'''
	def login_exit(self):
		My_method.My_id(self,module_info['账户'],'click')
		My_method.My_id(self,account['更多'],'click')
		My_method.My_id(self,module_info['退出'],'click')
		My_method.My_id(self,'com.yourenkeji.shenghuidai:id/positiveButton','click')
		logging.info('退出账号成功')

	'''判断是否登录'''
	def login_turn_or_flase(self,panduan_login,name,password):
		My_method.My_id (self, module_info ['账户'], 'click')
		if panduan_login=='判断登录':
			self.driver.implicitly_wait (3)
			try:

				a=My_method.My_id(self,zhuce['登录'],'获取元素')
				if a :
					My_method.loginCode (self, name, password)
			except Exception:
				logging.info('已经登录了哦')

	'''封装一个多次返回的方法'''
	def app_back(self,cishu=1):
		for i in range(cishu):
			self.driver.back()


class myMethod (object):
	'''封装一个随机生成电话号码的方法,默认方法首位字母为1，其余十位随机'''

	def randomTel (self):
		i = 1
		listUsername = ['1']
		while i <= 10:
			Usernamecode = str (random.choice (range (10)))
			listUsername.append (Usernamecode)
			i += 1
		return ''.join (listUsername)

	'''等待定位元素'''
	def wait_time (self, resourceid, waitTime = None):
		try:
			if waitTime == None:
				waitTime = 10
			WebDriverWait (waitTime).until (lambda driver: driver.find_element_by_id (resourceid))
			logging.info (u'>>>检测到{},页面未跳转成功'.format (resourceid))
		except Exception as f:
			print (f)
			logging.info (u'>>>未检测到{},页面跳转成功'.format (resourceid))

'''封装一个解锁手机功能'''
class Pingmu_unlock_the_screen(object):
	def pingmu_jiesuo(self):
		b = os.popen ('adb shell dumpsys window policy|grep mScreenOnFully')
		a = b.read ().strip ()
		deng = a [-5:]
		logging.info (f'判断是否锁屏{deng}')
		if deng == str ('false'):
			logging.info('屏幕是灭的,等待解锁')
			os.popen ('adb shell input keyevent 26')
			time.sleep (1)
			os.popen ('adb shell input swipe 50 1000 50 0 100')
		else:
			os.popen ('adb shell input swipe 50 1000 50 0 100')
			logging.info('不是锁屏状态,可直接执行项目哦')

	def App_jiesuo(self):
		list_pwd = self.driver.find_elements_by_class_name ("android.widget.ImageView")
		logging.info(list_pwd)
		try:
			TouchAction (self.driver).press (list_pwd [0]).move_to (list_pwd [3]).move_to (list_pwd [6]).wait (100).move_to (
				list_pwd [7]).wait (100).move_to (list_pwd [8]).release ().perform ()
			time.sleep (2)
			logging.info ('解锁成功')
			return True
		except Exception:
			logging.info('解锁失败')

'''封装一个滑动的方法'''
class Huadong(object):
	def Getsize (self):
		x = self.driver.get_window_size () ['width']
		y = self.driver.get_window_size () ['height']
		logging.info(x,y)
		return x, y
	def huadong(self,fangxiang,huadong_time):
		screen_size = Huadong.Getsize (self)
		if fangxiang=='上':
			x1=int(screen_size[0]*0.5)
			y1=int(screen_size[1]*0.75)
			y2=int(screen_size[1]*0.25)
			zuobiao='手机坐标为：'
			logging.info('%s,x=(%s%s),y=(%s%s),滑动了%s毫秒'%(zuobiao,x1,y1,x1,y2,huadong_time))
			return self.driver.swipe (x1, y1, x1, y2, huadong_time)
		elif fangxiang=='下':
			x2 = int (screen_size [0] * 0.5)
			y3 = int (screen_size [1] * 0.25)
			y4 = int (screen_size [1] * 0.75)
			zuobiao = '手机坐标为：'
			logging.info ('%s,x=(%s%s),y=(%s%s),滑动了%s毫秒' % (zuobiao, x2, y3, x2, y4,huadong_time))
			return self.driver.swipe (x2, y3, x2, y4, huadong_time)
		elif fangxiang=='左':
			x3 = int (screen_size [0] * 0.75)
			y5 = int (screen_size [1] * 0.5)
			x4 = int (screen_size [0] * 0.05)
			zuobiao = '手机坐标为：'
			logging.info ('%s,x=(%s%s),y=(%s%s),滑动了%s毫秒' % (zuobiao, x3, y5, x4, y5,huadong_time))
			return self.driver.swipe (x3, y5, x4, y5, huadong_time)
		elif fangxiang=='右':
			x5 = int (screen_size [0] * 0.05)
			y6 = int (screen_size [1] * 0.5)
			x6 = int (screen_size [0] * 0.75)
			zuobiao = '手机坐标为：'
			logging.info ('%s,x=(%s%s),y=(%s%s),滑动了%s毫秒' % (zuobiao, x5, y6, x6, y6,huadong_time))
			return self.driver.swipe (x5, y6, x6, y6, huadong_time)
		else:
			logging.info("写错了哦，无法滑动")
'''截图功能'''
class jietu(object):
	def jietu_picture(name):
		path = '/Users/yuchengtao/PycharmProjects/shenghuidai/SHD_automation/panda_picture/'
		os.popen ("adb wait-for-device")
		os.popen ("adb shell /system/bin/screencap -p /data/local/tmp/tmp.png")
		os.popen ("adb pull /data/local/tmp/tmp.png " + path + name + ".png")
		os.popen ("adb shell rm /data/local/tmp/tmp.png")
		logging.info ('success,已经成功的保存在当前目录下')
