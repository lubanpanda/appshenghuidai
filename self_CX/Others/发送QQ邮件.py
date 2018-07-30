#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
# @Email :  84305510@qq.com
# @Time : 2018/3/26 15:23
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

import requests

my_sender = '1007596772@qq.com'
my_user = "84305510@qq.com"


def weather (city_name):
	url = 'https://www.sojson.com/open/api/weather/json.shtml?city=' + city_name
	UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
	weather_shuju = requests.get (url, headers = {'User-Agent': UA})
	weather_info = weather_shuju.json ()
	print (weather_info)
	return weather_info


def mail (news):
	rets = True
	try:
		# with open('QQ.text','r') as e:
		#     news=e.read()
		msg = MIMEText (news)
		msg ['From'] = formataddr (["熊猫", my_sender])
		msg ['To'] = 'entry'.join (my_user)
		msg ['Subject'] = "天气预报 "
		server = smtplib.SMTP_SSL ('smtp.qq.com', 465)
		server.login (my_sender, "")
		server.sendmail (my_sender, [my_user, ], msg.as_string ())
		server.set_debuglevel (1)  # 数字是1的话是开启debug模式
		server.quit ()
	except Exception:
		rets = False
	return rets


if __name__ == '__main__':
	a = weather ('太原')
	ret = mail (a)
	if ret:
		print (f"ok,给{my_user}邮件发送成功，,请注意查收")
	else:
		print ("发送失败")
