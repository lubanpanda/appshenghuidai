#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda

from ATM.core import auth
from ATM.core.accounts import load_current_balane
from ATM.core.transaction import mak_transaction
from ATM.log.atm_log import *


#临时的账户数据记录
user_data={
	'account_id':None,#账户的名字
	'is_authenticated':False,#验证是否通关
	'account_data':None #账户详情
}
def account_info(acc_data=user_data['account_data']):

	log().info(f"-------你的账户信息如下---------\,账户:{acc_data['account_id']},密码:{acc_data['account_data']['password']},总资产:{acc_data['account_data']['balance']},利息:{acc_data['account_data']['interest']},卡的有效期:{acc_data['account_data']['expire_date']}")
	print("请问是否还需要其他服务，是的话请选择服务菜单")
	interactive(acc_data)

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

		if user_option in menu_dic:
			menu_dic[user_option](acc_data)

		else:
			print('输入的序号错误，请重新输入')



def logout(acc_data):
	pass

def pay_check(acc_data):
	pass

def repay(acc_data):
	pass

def transfer(acc_data):
	pass

def withdrae(acc_data):
	account_data=load_current_balane(acc_data['account_id'])
	print(account_data)
	infp=f"""
	---------欢迎使用panda银行系统-----------
	你的信用值是：{account_data['credit']}
	你的可取款金额是：{account_data['balance']}
	"""
	print(infp)
	back_flag=False
	while not back_flag:
		qukuan_money=input("请输入你要存款的金额:").strip()
		if len(qukuan_money)>0 and qukuan_money.isdigit():
			new_balance=mak_transaction(account_data,'repay',qukuan_money)
			if new_balance:
				print("取钱成功")
		else:
			print("你输入的金额有误，请重新输入")
			continue


def run():
	acc_data=auth.acc_login(user_data)
	if user_data['is_authenticated']:
		user_data['account_data']=acc_data
		interactive(user_data)