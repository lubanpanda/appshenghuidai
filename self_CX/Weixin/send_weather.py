#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/2/15 14:23
import itchat
import requests
from bs4 import BeautifulSoup


class weixin(object):
	def __init__(self):
		itchat.auto_login (hotReload = True)
		self.friends = itchat.get_friends (update = True) [0:]
		self.myUserName=itchat.get_friends(update=True)[0]["UserName"]


	def send_weixin(self,Tousername):
		"""
		:param Tousername: 发送的人
		:param name: 备注、微信号、昵称
		:param message: 发送消息的内容
		:return:发送微信消息
		 ***使用search_friends方法可以搜索用户，有四种搜索方式：***
		   1. 仅获取自己的用户信息
		   2. 获取特定UserName的用户信息
		   3. 获取备注、微信号、昵称中的任何一项等于name键值的用户
		   4. 获取备注、微信号、昵称分别等于相应键值的用户
		"""
		Help = """先生/女士你好：
		欢迎来到机器人天气实施查询小程序，请输入你想查询的城市：
		"""
		itchat.send(msg =Help,toUserName =Tousername)

to_name = []
@itchat.msg_register(itchat.content.TEXT)
def getcity(msg):
	myUserName = itchat.get_friends (update = True) [0] ["UserName"]
	if msg['ToUserName']!=myUserName:
		return
	print(msg['Text'])
	city_name=msg['Text']
	too_name=msg['FromUserName']
	try:
		if to_name[-1] ==too_name:
			to_name.append (too_name)
		else:
			a.send_weixin(too_name)
			to_name.append (too_name)
	except:
		a.send_weixin (too_name)
		to_name.append (too_name)
	if len(to_name)==1:
		print(len(to_name))
	else:
		with open ('chengshi.txt') as f:
			chengshi_name = f.read()
		if 6 >= len(city_name) >= 2:
			names=city_name+'市'
			if names in chengshi_name :
				results = weather (city_name)
				itchat.send(results,msg['FromUserName'])
			elif not city_name or not names in chengshi_name:
				itchat.send ('请输入正确的城市名称', msg['FromUserName'])
		else:pass
def weather(city_name):
	url='http://m.sohu.com/weather/?city='+city_name
	UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
	weather_shuju=requests.get(url,headers={'User-Agent':UA})
	html=weather_shuju.text
	soup=BeautifulSoup(html,'html.parser')
	now_wendu=soup.find('p',class_='cur').string
	up_wendu=soup.find('em',class_='highest').string
	low_wendu=soup.find('em',class_='lowest').string
	xiangqing=soup.find('em',class_='stat').string
	PM=soup.find('p',class_='tit').string
	fengli=soup.find('div',class_='pm')
	feng,shidu=map(lambda ab:ab.string, fengli)
	xiangxi_weather_info= f'城市：{city_name}\n' \
	                      f'现在的温度：{now_wendu}\n' \
	                      f'最高气温：{up_wendu}\n' \
	                      f'最低温度：{low_wendu}\n' \
	                      f'天气情况:{xiangqing}\n' \
	                      f'PM值：{PM}\n' \
	                      f'舒适指数：{feng,shidu}'
	print(xiangxi_weather_info)
	return xiangxi_weather_info

if __name__ == '__main__':
	a=weixin()
	itchat.run()