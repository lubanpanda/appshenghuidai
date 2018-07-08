#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"


import time
from ATM.conf import settings
from ATM.core.accounts import dump_account, loads_current_balane, dumps_account, save_red_info
import random
import os


def mak_transaction(account_data,tran_type,amount):
	"""
	:param account_data: 账户信息
	:param tran_type: 交易类型
	:param amount:要交易的钱
	:return:
	"""
	amount=float(amount)
	if tran_type in settings.TRANSACTION_TYPE:
		interest=amount * settings.TRANSACTION_TYPE[tran_type]['interest']#利息
		old_balance=account_data['balance']
		if settings.TRANSACTION_TYPE[tran_type]['action']=='plus':
			new_balance=old_balance+interest+amount
			print(f'现在是{new_balance}元')
		elif settings.TRANSACTION_TYPE[tran_type]['action']=='minus':
			new_balance=old_balance-interest-amount
			if new_balance<0:
				print(f"你的额度不够，你现在的余额是{new_balance}")
				return
		account_data['balance']=new_balance
		dump_account(account_data)
		return account_data
	else:
		print("交易类型没有被找到")


def mak_reimbursement(account_data,shoukuan_id):
	"""
	:param account_id:转账人
	:param shoukuan_id: 接收人
	:return:
	"""
	now_balanes=account_data['balance']
	too_info= loads_current_balane (shoukuan_id)
	now_too_balanes=too_info['balance']
	zhuan_money=float(input("请输入要转账的金额").strip())
	if zhuan_money>0:
		now_balanes -= float(zhuan_money)
		now_too_balanes += float(zhuan_money)
		account_data['balance']=now_balanes
		too_info['balance']=now_too_balanes
		dump_account(account_data)
		dumps_account(too_info)
		print (f"转账成功,自己金额还剩余{account_data['balance']},现在借款方为{too_info['balance']}元")
		return account_data,too_info
	else:
		print("你输入的金额有误，请重新输入")


def Save_gade_money(account_data,money):
	account_data ['balance'] -= float(money)
	dump_account(account_data)
	print('现在的金额为%s元'%account_data ['balance'])
	return account_data,money


def qiang_red(Q_money, cishu):
	nowtime = time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime ())
	total = float (Q_money)
	num = int (cishu)
	min = 0.01
	reds_info=[]
	if num < 1:
		return
	if num == 1:
		print ("第%d个人拿到红包数:%.2f" % (num, total))
		return
	i = 1
	totalMoney = total
	while i < num:
		max = totalMoney - min * (num - i)
		k = int ((num - i) / 2)
		if num - i <= 2:
			k = num - i
		max = max / k
		monney = random.randint (int (min * 100), int (max * 100))
		monney = float (monney) / 100
		totalMoney -= monney
		aaa=("第%d个人拿到红包为:%.2f" % (i, monney)+os.linesep)
		reds_info.append(aaa)
		print(aaa)
		i += 1
	bbb=("第%d个人拿到红包为:%.2f" % (i, totalMoney)+os.linesep)
	reds_info.append(bbb)
	print(bbb)
	for i in reds_info:
		save_red_info(i,nowtime)