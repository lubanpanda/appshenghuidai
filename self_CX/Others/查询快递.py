#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import json

import requests

"""查询运送的快递分类"""


def get_express_type (postid):
	url = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text={0}'.format (postid)
	print (url)
	rs = requests.get (url)
	kd_type_info = json.loads (rs.text)
	kd_type = kd_type_info ['auto'] [0] ['comCode']
	print (kd_type, postid)
	return kd_type, postid


"""实际查询物流"""


def execute_data_query (type, postid):
	url = f'http://www.kuaidi100.com/query?type={type}&postid={postid}'
	rs = requests.get (url)
	kd_info = json.loads (rs.text)
	msg = kd_info ['message']
	if msg == 'ok':
		print ('您的快递%s物流信息如下：' % postid)
		data = kd_info ['data']
		for data_dict in data:
			time = data_dict ['time']
			context = data_dict ['context']
			print ('时间：%s %s' % (time, context))
	else:
		if msg == '参数错误':
			print ('您输入信息有误，请重输：')
		else:
			print (msg)


def main ():
	print ('**欢迎您登录快递查询系统**')
	print ('-' * 30)
	print ('** 1. 请输入您的快递单号 **')
	print ('** 0. 退出查询系统       **')
	print ('-' * 30)
	order = input ('查询请输入1退出请输入0：')
	if order == '1':
		postid = input ('请输入您的快递单号：')
		type, postid = get_express_type (postid)
		execute_data_query (type, postid)
	elif order == '0':
		exit ()
	else:
		print ('!!!!!您的指令输入有误，请重新输入：<---------')


if __name__ == '__main__':
	main ()
