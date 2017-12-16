#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
import json
import requests
from appium import webdriver
import os
import time
from time import sleep
import threading
import datetime
timestamp = time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime ())
def Shijiancha(fune):
	"""
	:param fune:
	:return:
	"""
	def zhuang():
		"""
		执行的时间
		"""
		star_time=datetime.datetime.now()
		fune()
		stop_time=datetime.datetime.now()
		print('花费时间为：', stop_time - star_time)
	return zhuang
def connnect_ipad_device():
	"""
	定义测试平台的属性
	:return: device及参数
	"""
	pingmu_jiesuo()
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
def pingmu_jiesuo():
	b = os.popen ('adb shell dumpsys window policy|grep mScreenOnFully')
	a = b.read ().strip ()
	deng = a [-5:]
	if deng == str ('false'):
		print ('屏幕是灭的,等待解锁')
		os.popen ('adb shell input keyevent 26')
		time.sleep (1)
		os.popen ('adb shell input swipe 50 1000 50 0 100')
	else:
		os.popen ('adb shell input swipe 50 1000 50 0 100')
		print ('不是锁屏状态,可直接执行项目哦')

def getsize():
	"""
	获得手机屏幕大小
	:return:
	"""

	x = device.get_window_size()['width']
	y = device.get_window_size()['height']
	return x, y


def swipe_to_up(duration):
	"""
	屏幕向上滑动
	:param duration: 滑动的毫秒数值
	:return:
	"""
	screen_size = getsize()
	# X坐标
	x1 = int(screen_size[0] * 0.5)
	# 起始Y坐标
	y1 = int(screen_size[1] * 0.75)
	# 终点Y坐标
	y2 = int(screen_size[1] * 0.25)
	device.swipe(x1, y1, x1, y2, duration)


def swipe_to_down(duration):
	"""
	屏幕向下滑动
	:param duration: 滑动的毫秒数值
	:return:
	"""

	screen_size = getsize()
	x1 = int(screen_size[0] * 0.5)
	y1 = int(screen_size[1] * 0.25)
	y2 = int(screen_size[1] * 0.75)
	device.swipe(x1, y1, x1, y2, duration)


def swipe_to_left(duration):
	"""
	屏幕向左滑动
	:param duration: 滑动持续的毫秒值
	:return:
	"""
	screen_size = getsize()
	x1 = int(screen_size[0] * 0.75)
	y1 = int(screen_size[1] * 0.5)
	x2 = int(screen_size[0] * 0.05)
	device.swipe(x1, y1, x2, y1, duration)


def swipe_to_right(duration):
	"""
	屏幕向右滑动
	:return:
	"""
	screen_size = getsize()
	x1 = int(screen_size[0] * 0.05)
	y1 = int(screen_size[1] * 0.5)
	x2 = int(screen_size[0] * 0.75)
	device.swipe(x1, y1, x2, y1, duration)


PATH = lambda p: os.path.abspath (p)
def screenshot (name):
	"""
	截取手机屏幕
	:param name:相片文件名
	:return:
	"""
	path = PATH (os.getcwd () + "/screenshot")
	os.popen ("adb wait-for-device")
	os.popen ("adb shell screencap -p /data/local/tmp/tmp.png")
	if not os.path.isdir (PATH (os.getcwd () + "/screenshot")):
		os.makedirs (path)
	os.popen ("adb pull /data/local/tmp/tmp.png " + PATH (path + "/" + name+timestamp + ".png"))
	os.popen ("adb shell rm /data/local/tmp/tmp.png")
	print('success,已经成功的保存在当前目录下')
def faxian_all():
	"""
	点击积分商场的兑换记录
	:return:
	"""
	device.implicitly_wait(30)
	device.find_elements_by_class_name ('android.widget.RadioButton') [2].click ()
	u'平台数据'
	device.find_elements_by_class_name('android.widget.TextView')[0].click()
	time.sleep(2)
	device.back()
	u'安全保障'
	device.find_elements_by_class_name ('android.widget.TextView') [1].click ()
	for a in range(6):
		# noinspection PyAssignmentToLoopOrWithParameter
		for i in range(2):
			device.find_elements_by_class_name('android.widget.Image')[1 + a].click()
	device.back()
	u'查看积分'
	device.find_element_by_id('com.yourenkeji.shenghuidai:id/jifenshangcheng').click()
	device.find_elements_by_class_name('android.widget.Image')[0].click()
	device.back()
	for a in range(8):
		if a >= 5:
			swipe_to_up(1000)
			device.find_elements_by_class_name('android.widget.Image')[2 + a].click()
			time.sleep(2)
			device.back()
		else:
			device.find_elements_by_class_name ('android.widget.Image') [2 + a].click ()
			time.sleep(2)
			device.back()
	device.back()
	u'活动中心'
	device.find_element_by_id('com.yourenkeji.shenghuidai:id/huodongzhongxin').click()
	device.back()
	'两个图片'
	device.find_element_by_id('com.yourenkeji.shenghuidai:id/faxian_xshb_iv').click()
	time.sleep(2)
	device.back()
	device.find_element_by_id('com.yourenkeji.shenghuidai:id/faxian_xydzp_iv').click()
	time.sleep(2)
	device.back()
	u'发现更多'
	url = "https://api.shenghuidai.com:8012/v1/news/media/all"

	headers = {'Cache-Control': "no-cache", 'Postman-Token': "3949fa4d-8390-539d-dee7-a28c5565b02a"}

	response = requests.request ("POST", url, headers = headers)
	response = json.loads (response.text)
	xinwen_geshu = []
	if response ['code'] == str (10000):
		print ("请求接口数据成功")
		xinwen_geshu = []
		for a in response ['content']:
			xinwen_geshu.append (len (a))
	else:
		print ("失败喽")
	# noinspection PyCompatibility
	print (f"一共有{len(xinwen_geshu)}条新闻,前6条显示就可以默认都显示正常了")
	xinwen_shuliang = int (len (xinwen_geshu))
	device.find_elements_by_class_name ('android.widget.TextView') [6].click ()
	for a in range (xinwen_shuliang):
		if a <= 6:
			device.find_elements_by_class_name ('android.widget.ImageView') [a + 1].click ()
			time.sleep (2)
			swipe_to_up (1000)
			device.back ()
		else:
			pass
	device.back()

def All_shouye():
	"""
	首页的四个小模块查看
	:return:
		"""
	device.implicitly_wait(30)
	device.find_element_by_id('com.yourenkeji.shenghuidai:id/boluos_bt_home').click()
	# u'投资攻略'
	# device.find_elements_by_class_name ('android.widget.TextView') [0].click ()
	# time.sleep (5)
	# for j in range (3, 10, 2):
	# 	device.find_elements_by_class_name ('android.view.View') [j].click ()
	# for a in range (4):
	# 	device.back ()
	# time.sleep (2)
	# u'新手指引'
	# device.find_elements_by_class_name('android.widget.TextView')[1].click()
	# time.sleep(2)
	# device.back()
	# u'邀请好友'
	# # TODO 测试好了一会回来改这里
	# device.find_elements_by_class_name('android.widget.TextView')[2].click()
	# device.find_element_by_id ('com.yourenkeji.shenghuidai:id/webView_bt_share').click ()
	# time.sleep (3)
	# # '点击QQ'
	# device.find_elements_by_class_name ('android.widget.ImageButton') [2].click ()
	# time.sleep (3)
	# '分享给我的电脑'
	# device.find_elements_by_class_name ('android.widget.RelativeLayout') [5].click ()
	# '发送'
	# device.find_element_by_id ('com.tencent.mobileqq:id/dialogRightBtn').click ()
	# '返回'
	# device.find_element_by_id ('com.tencent.mobileqq:id/dialogLeftBtn').click ()
	# '活动规则'
	# device.find_elements_by_class_name('android.view.View')[1].click()
	# time.sleep(3)
	# device.find_elements_by_class_name('android.view.View')[9].click()
	# device.back()
	u'每日签到'
	device.find_elements_by_class_name('android.widget.TextView')[3].click()
	u'签到'
	device.find_elements_by_class_name ('android.view.View')[52].click()
	try:
		device.find_elements_by_class_name('android.widget.Button')[0].click()
	except Exception:
		print('保证签到成功就可以了')
	print('已经签到完成')
	u'签到规则'
	device.find_elements_by_class_name('android.widget.Image')[1].click()
	swipe_to_up(4000)
	time.sleep(3)
	device.back()


def ture_or_flase_login():
	"""
	判断是否登录
	:return:
	"""
	# noinspection PyBroadException
	try:
		a=device.find_elements_by_class_name ('android.widget.TextView')[14]
		print(a)
		return True
	except Exception :
		return False


def login():
	"""
	登录账号或者切换账号
	:return:
	"""
	# 等待启动，设置程序休眠/防止手机反应慢卡死
	time.sleep(5)
	#点击账户
	device.find_elements_by_class_name ('android.widget.RadioButton') [3].click ()

	#点击更多
	if ture_or_flase_login () is True:
		print('准备开始切换账户了')
		device.find_elements_by_class_name ('android.widget.TextView') [14].click()
		device.find_elements_by_class_name('android.widget.Button')[0].click()
		#确定

		device.find_elements_by_class_name('android.widget.Button')[0].click()
		# 点击账户
		device.find_elements_by_class_name ('android.widget.RadioButton') [3].click ()
		#登录
		device.find_elements_by_class_name('android.view.View')[6].click()
		'登录账户'
		device.find_elements_by_class_name ('android.widget.EditText') [0].clear()
		login_ip=device.find_elements_by_class_name('android.widget.EditText')[0]
		device.set_value(login_ip,'18519291259')
		device.find_elements_by_class_name('android.widget.Button')[0].click()
		#密码
		password=device.find_elements_by_class_name('android.widget.EditText')[0]
		device.set_value(password,'111111')
		device.find_elements_by_class_name('android.widget.Button')[0].click()
		#跳过手势密码
		try:
			device.find_element_by_id('com.yourenkeji.shenghuidai:id/img_cancel').click()
		except Exception as e:
			print(e)
			device.back()
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
		device.find_element_by_id ('com.yourenkeji.shenghuidai:id/img_cancel').click ()

@Shijiancha
def gonggao():
	"""
	公告
	:return:
	"""
	device.implicitly_wait(10)
	swipe_to_up (1000)
	device.find_elements_by_class_name('android.widget.LinearLayout')[9].click()
	device.back()


@Shijiancha
def hongbao():
	"""
	判断优惠券的个数来进行操作,测试版本的优惠券
	:return:
	"""
	url = "http://apitest.shenghuidai.com:8012/v1/asset/18519291259/red/pocket"
	headers = {'cache-control': "no-cache", 'postman-token': "78531346-aad3-2a2b-57bb-b886fe3718ff"}
	response = requests.request ("POST", url, headers = headers)
	if response.status_code==200:
		print("请求成功")
	else:
		print("请求失败，请查看网络配置")
	hongbao_info=json.loads(response.text)
	hongbao_geshu=[]
	for z in hongbao_info['content']:
		hongbao_geshu.append(len(z))
	url = "http://apitest.shenghuidai.com:8012/v1/asset/18519291259/rate/pocket"
	headers = {'cache-control': "no-cache", 'postman-token': "a5aa815a-8c15-5674-9ead-4b1340b46cbf"}
	response = requests.request ("POST", url, headers = headers)
	if response.status_code==200:
		print("请求成功")
	else:
		print("请求失败，请查看网络配置")
	jiaxiquan_info = json.loads (response.text)
	jiaxiquan_geshu = []
	for z in jiaxiquan_info ['content']:
		jiaxiquan_geshu.append (len (z))
	#print (len (jiaxiquan_geshu))
	device.implicitly_wait(8)
	device.find_elements_by_class_name('android.widget.RadioButton')[3].click()
	device.find_elements_by_class_name('android.widget.TextView')[10].click()
	if len(hongbao_geshu) >0:
		print('有红包,红包个数为：',len(hongbao_geshu))
		device.find_elements_by_class_name ('android.widget.TextView') [3].click ()
		if len (jiaxiquan_geshu) > 0:
			print ("有加息券，个数为：", len (jiaxiquan_geshu))
			device.back ()
	else:
		print("没有红包")
		device.find_elements_by_class_name('android.widget.TextView')[3].click()
		if len(jiaxiquan_geshu)>0:
			print("有加息券，个数为：",len(jiaxiquan_geshu))
			device.back()


@Shijiancha
def cipher():
	"""
	交易密码
	:return:
	"""
	for c in range (6):
		new_password = device.find_elements_by_class_name ('android.widget.TextView') [c+11]
		new_password.click ()

	#shouye_to=device.find_elements_by_class_name('android.widget.Button')
	shouye_to=device.find_element_by_id('com.yourenkeji.shenghuidai:id/bidSucess_bt')
	time.sleep(5)
	if shouye_to:
		shouye_to.click()
		print('密码正确')
	else:
		print('密码错误,正在尝试第二种密码......')
		for o in range(6):
			device.find_elements_by_class_name ('android.widget.TextView') [22].click ()
		for c in range (6):
			password = device.find_elements_by_class_name ('android.widget.TextView') [0]
			password.click ()
		print("密码正确，交易成功")
		device.find_elements_by_class_name('android.widget.Button')[0].click()


@Shijiancha
def new_toubiao():
	"""
	投资新手标
	:return:
	"""
	device.implicitly_wait (10)
	device.find_elements_by_class_name('android.widget.RelativeLayout')[1].click()
	touzi_money=device.find_elements_by_class_name('android.widget.EditText')[0]
	device.set_value(touzi_money,1000)
	device.find_elements_by_class_name('android.widget.Button')[1].click()
	new_biao_youhui=device.find_elements_by_class_name('android.widget.TextView')[21].click()
	if new_biao_youhui:
		print ("可以点击使用优惠券，请确认是否是新手或了解业务需求")
	else:
		print ("验证正确，不能使用优惠券")
	new_buy=device.find_elements_by_class_name('android.widget.Button')[0].click()
	if new_buy:
		print("你不是新手，可以购买")
		cipher()
	else:
		print("你已经不是新手了，不能购买新手标了")
	device.back()
	device.back()



def toubiao():
	"""
	投资普通标
	:return:
	"""
	time.sleep(8)
	swipe_to_up(1000)
	device.find_elements_by_class_name('android.widget.RelativeLayout')[1].click()
	jine=device.find_elements_by_class_name('android.widget.EditText')[0]
	device.set_value(jine,1000)
	device.find_elements_by_class_name('android.widget.Button')[1].click()
	device.find_elements_by_class_name('android.widget.Button')[0].click()
	#输入支付密码
	cipher()
def timeout():
	"""
	支付密码超时处理
	:return:
	"""
	print("输入超时，默认不做提现处理."+os.linesep)
	other()

def all_account(money):
	"""
	账户页面的操作
	:param money:提现的金额
	:return:
	"""
	device.implicitly_wait(30)
	device.find_elements_by_class_name('android.widget.RadioButton')[3].click()
	'隐藏金额'
	device.find_element_by_id ('com.yourenkeji.shenghuidai:id/my_eyes_checkbox').click ()
	'账户信息'
	device.find_element_by_id ('com.yourenkeji.shenghuidai:id/imageView1').click ()
	'账户余额'
	device.find_element_by_id ('com.yourenkeji.shenghuidai:id/my_zongzichan_img_right').click ()
	'冻结金额'
	device.find_element_by_id ('com.yourenkeji.shenghuidai:id/my_zongzichan_img_dongjieyue').click ()
	device.find_element_by_id ('com.yourenkeji.shenghuidai:id/positiveButton').click ()
	device.back()
	#投资记录
	device.find_elements_by_class_name('android.widget.TextView')[5].click()
	sleep(2)
	device.find_elements_by_class_name('android.widget.TextView')[2].click()
	device.back()
	device.back()
	#回款日历
	device.find_elements_by_class_name('android.widget.TextView')[6].click()
	device.back()
	t = threading.Timer (10.0, timeout)
	t.start ()
	#select_tixian = int (input ("体现输入1，不提醒输入2，请在10S内输入:"+os.linesep))
	select_tixian=int(2)
	if  select_tixian==1:
		#体现
		t.cancel()
		device.find_elements_by_class_name('android.widget.TextView')[8].click()
		tixian_money=device.find_elements_by_class_name('android.widget.RelativeLayout')[2]
		tixian_money.click()
		tixian_money.send_keys(money)
		while True:
			if money<0:
				print("请输入正确金额")
				break
			elif money<100:
				print("提现金额最低为100元")
				break
			else:
				print("金额输入正确，请进行下一步操作")
				break
		device.find_elements_by_class_name('android.widget.Button')[0].click()
		for b in range (6):
			new_password = device.find_elements_by_class_name ('android.widget.Button') [b]
			new_password.click ()
		time.sleep(2)
		device.find_elements_by_class_name('android.widget.Button')[0].click()

	else:
		t.cancel()
		print("不做提现动作")

	other()

def other():
	"""
	资金记录到更多
	:return:
	"""
	#资金记录
	time.sleep(2)
	device.find_elements_by_class_name('android.widget.TextView')[9].click()
	device.back()
	'''
	#安全管理
	device.find_elements_by_class_name('android.widget.TextView')[12].click()
	device.find_elements_by_class_name('android.widget.RelativeLayout')[1].click()
	#记得支付密码
	device.find_elements_by_class_name('android.widget.RelativeLayout')[2].click()
	yuan_key=device.find_elements_by_class_name('android.widget.EditText')[0]
	device.set_value(yuan_key,123456)
	new_key=device.find_elements_by_class_name('android.widget.EditText')[1]
	device.set_value(new_key,123456)
	new_key_too=device.find_elements_by_class_name('android.widget.EditText')[2]
	device.set_value(new_key_too,123456)
	device.find_elements_by_class_name('android.widget.Button')[0].click()
	time.sleep(2)
	#设置手势密码
	time.sleep(2)
	device.find_elements_by_class_name('android.widget.RelativeLayout')[2].click()
	device.back()
	device.back()
	time.sleep(2)
	'''
	device.find_elements_by_class_name('android.widget.TextView')[13].click()
	device.back()
	time.sleep(2)
	device.find_elements_by_class_name('android.widget.TextView')[14].click()
	device.back()

if __name__ == '__main__':
    device=connnect_ipad_device()
    device.implicitly_wait(20)
    All_shouye()