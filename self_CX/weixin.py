#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
# @Email :  84305510@qq.com
# @Time : 2018/2/15 14:23
"""
微信信息数据
"""
import itchat
itchat.auto_login(hotReload = True)
friends=itchat.get_friends(update = True)[0:]
# print(friends)
friedd_data=[]
for friend in friends[1:]:
	niceName=friend['NickName']#网民
	remarkName=friend['RemarkName']#备注名
	city=friend['City']#地点
	sex=friend['Sex']#性别1为男
	province=friend['Province']#省份
	signature=friend['Signature']#签名
	f_d={
		'niceName':friend ['NickName'],
		'remarkName' : friend ['RemarkName'],
		'city' : friend ['City'],
		'sex' : friend ['Sex'],
		'province' : friend ['Province'],
		'signature' : friend ['Signature']
	}
	friedd_data.append(f_d)
print(friedd_data)