#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import datetime
import json
import os
from os import walk

from ATM.conf import settings
from ATM.core import db_handle
from ATM.core.accounts import dump_account

BASE_DIR = os.path.dirname (os.path.dirname (os.path.abspath (__file__)))


def brrow_moeny (add_count_id, borrowing_moeny, brrowing_yuefen):
	"""
	:param add_count_id: 账户ID
	:param borrowing_moeny: 借款金额
	:param brrowing_yuefen: 借款的月份
	:return:
	"""
	nowtime = datetime.datetime.today ()
	brrowing_yuefen = int (brrowing_yuefen)
	borrowing_moeny = int (borrowing_moeny)
	shiji_moeny = borrowing_moeny * (1 + brrowing_yuefen / 100)
	db_path = db_handle.db_handle (settings.DATABASE)
	account_file = f"{db_path}/{add_count_id}.json"
	if os.path.isfile (account_file) and add_count_id != 'admin':
		with open (account_file, 'r') as f:
			account_data = json.load (f)
			date = nowtime + datetime.timedelta (days = 30)
			account_data ['jiekuan_money'] += shiji_moeny
			account_data ['jiekuan_date'] = str (date.date ())
			account_data ['balance'] += shiji_moeny
			dump_account (account_data)
			print (f"借款成功,你已成功借款{account_data ['jiekuan_money']}元，还款日期是{account_data ['jiekuan_date']}")
	else:
		print ('借款失败,原因未知')


def reimbursement (add_count_id, huankuan_money, all_money, jiekuan_money):
	"""
	:param add_count_id:账户ID
	:param huankuan_money: 还款金额
	:param all_money: 账户总金额
	:param jiekuan_money: 借款的金额
	:return:还款
	"""
	if huankuan_money <= jiekuan_money:
		if all_money - jiekuan_money <= 0:
			db_path = db_handle.db_handle (settings.DATABASE)
			account_file = f"{db_path}/{add_count_id}.json"
			if os.path.isfile (account_file) and add_count_id != 'admin':
				with open (account_file, 'r') as f:
					account_data = json.load (f)
					account_data ['balance'] = all_money - huankuan_money
					account_data ['jiekuan_money'] = jiekuan_money - huankuan_money
					account_data ['credit'] += 1
					dump_account (account_data)
					print ('还款成功,你的信用值+1')
				if account_data ['jiekuan_money'] == 0:
					account_data ['jiekuan_money'] = 0
					account_data ['jiekuan_date'] = 0
					dump_account (account_data)
		else:
			print ('还款后你的账户总资产将为负，所以不能进行还款，快快去搬砖存款吧')
	else:
		print ('还款金额不能大于借款金额')


def judge_money_date ():
	"""
	:return: 每次登陆时自动查看有无预期的账户
	"""
	now_time = datetime.datetime.today ().date ()
	for (dirpath, dirnames, filenames) in walk (f'{BASE_DIR}/db/accounts'):
		for file in filenames:
			if file.endswith ('json'):
				db_path = db_handle.db_handle (settings.DATABASE)
				account_file = f"{db_path}/{file}"
				with open (account_file, 'r') as f:
					account_data = json.load (f)
					account_data ['jiekuan_date'] if account_data ['jiekuan_date'] == 0 else print (
						f"账户{file[:-5]}没有进行即使还款，还款金额{account_data['jiekuan_money']},最后还款日期为{account_data['jiekuan_date']},请注意及时催交\n")
