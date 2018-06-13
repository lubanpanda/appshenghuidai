#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda

from ATM.core import auth
from ATM.log.atm_log import *


#临时的账户数据记录
user_data={
	'account_id':None,#账户的名字
	'is_authenticated':False,#验证是否通关
	'account_data':None #账户详情
}
def account_info(acc_data=user_data['account_data']):
	log().info(
					"-------你的账户信息如下---------\n"
	             f"账户:{acc_data['account_id']}\n"
	             f"密码:{acc_data['account_data']['password']}\n"
	             f"总资产:{acc_data['account_data']['balance']}\n"
	             f"利息:{acc_data['account_data']['interest']}\n"
	             f"卡的有效期:{acc_data['account_data']['expire_date']}\n"
	             )

def interactive(acc_data):
	menu='''
	---------welcome to panda bank----------
	1.账户信息
	2.还款功能
	3.取款功能
	4.转账
	5.账单
	6.退出
	
	'''
	menu_dic={
		'1':account_info,
		'2':repay,
		'3':withdrae,
		'4':transfer,
		'5':pay_check,
		'6':logout
	}

	exit_flag=False
	if not exit_flag:
		print(menu)
		user_option=input(">>>".strip())
		while True:
			if user_option in menu_dic:
				menu_dic[user_option](acc_data)
				break
			else:
				print('输入的序号错误，请重新输入')
				continue


def logout(acc_data):
	pass

def pay_check(acc_data):
	pass

def repay(acc_data):
	pass

def transfer(acc_data):
	pass

def withdrae(acc_data):

	pass

def run():
	acc_data=auth.acc_login(user_data)
	if user_data['is_authenticated']:
		user_data['account_data']=acc_data
		interactive(user_data)