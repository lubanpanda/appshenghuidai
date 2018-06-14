#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
from ATM.conf import settings
from ATM.core.accounts import dump_account, loads_current_balane, dumps_account


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
















