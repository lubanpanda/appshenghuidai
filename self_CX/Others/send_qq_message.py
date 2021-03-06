#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import requests
from bs4 import BeautifulSoup
from qqbot import QQBotSlot as qqbotslot, RunBot, qqbotsched


@qqbotsched (hour = '07', minute = '30')
def mytask (bot):
	gl = bot.List ('buddy', 'A大白兔奶糖')
	if gl is not None:
		for group in gl:
			bot.SendTo (group, str (Ai_tianqi ("南京")))


@qqbotslot
def onQQMessage (bot, contact, member, content):
	if '天气预报' in content:
		bot.SendTo (contact, str (tianqi (content [5:])))
	elif '新闻' in content:
		bot.SendTo (contact, str (sina ()))

	if '@ME' in content:
		bot.SendTo (contact, member.name + '你好，此消息由系统自动回复，有事请私聊？')

	elif content == "-stop":
		bot.Stop ()


def tianqi (name):
	url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + name
	tq_info = requests.get (url)
	tq_json = tq_info.json ()
	today = (tq_json.get ('data').get ('forecast') [0])  # 今天
	tomorrow = (tq_json.get ('data').get ('forecast') [1])  # 明天
	xiangqing = f"城市:{name}\n" \
	            f"今日日期：{today['date']}\n" \
	            f"天气状况：{today['type']}\n" \
	            f"最高温度：{today['high']}\n" \
	            f"最低温度：{today['low']}\n" \
	            f"明日日期：{tomorrow['date']}\n" \
	            f"天气状况：{tomorrow['type']}\n" \
	            f"最高温度：{tomorrow['high']}\n" \
	            f"最低温度：{tomorrow['low']}\n"
	return xiangqing


def sina ():
	url = 'https://news.sina.com.cn/society/'
	UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
	url_info = requests.get (url, headers = {'User-Agent': UA})
	info = url_info.content.decode ('utf-8')  # 转化编码格式
	soup = BeautifulSoup (info, 'html.parser')
	new_heads = soup.find ('div', class_ = 'right-content')
	bbb = new_heads.find_all ('a')
	news = []
	for i in bbb:
		news.append (i.text + ":" + i.get ('href'))

	bbb = f"1:{news[0]}\n" \
	      f"2:{news[1]}\n" \
	      f"3:{news[2]}\n" \
	      f"4:{news[3]}\n" \
	      f"5:{news[4]}\n"
	return bbb


def Ai_tianqi (name):
	url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + name
	tq_info = requests.get (url)
	tq_json = tq_info.json ()
	today = (tq_json.get ('data').get ('forecast') [0])  # 今天
	tomorrow = (tq_json.get ('data').get ('forecast') [1])  # 明天
	if today ['high'] > '30℃':
		info = '诶呀，今天天气好热呀，老婆别忘了带遮阳伞哦'
	elif '20℃' < today ['high'] < '25℃':
		info = "今天的天气有点小凉哦，多穿点衣服呢"
	xiangqing = f"城市:{name}\n" \
	            f"今日日期：{today['date']}\n" \
	            f"天气状况：{today['type']}\n" \
	            f"最高温度：{today['high']}\n" \
	            f"最低温度：{today['low']}\n" \
	            f"明日日期：{tomorrow['date']}\n" \
	            f"天气状况：{tomorrow['type']}\n" \
	            f"最高温度：{tomorrow['high']}\n" \
	            f"最低温度：{tomorrow['low']}\n" \
	            f"小傻瓜提示:{info}\n"
	return xiangqing


if __name__ == '__main__':
	RunBot (["-u", "somebody"])
