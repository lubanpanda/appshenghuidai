#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  84305510@qq.com
from bs4 import BeautifulSoup
import requests

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
	feng,shidu=map(lambda a:a.string,fengli)
	print(f'城市：{city_name}\n现在的温度：{now_wendu}\n最高气温：{up_wendu}\n最低温度：{low_wendu}\n天气情况:{xiangqing}\nPM值：{PM}\n舒适指数：{feng,shidu}')
if __name__ == '__main__':
    weather('佛山')
