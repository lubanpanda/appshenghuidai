#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
from ATM.conf import settings
from ATM.core.accounts import dump_account


def mak_transaction(account_data,tran_type,amount):
	"""

	:param account_data: 账户信息
	:param tran_type: 交易类型
	:param amount:要取得钱
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
