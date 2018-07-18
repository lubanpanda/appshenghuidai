#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import walk

__author__ = "panda  84305510@qq.com"

import json
import os
import datetime
from ATM.conf import settings
from ATM.core import db_handle
from ATM.core.accounts import dump_account

BASE_DIR = os.path.dirname (os.path.dirname (os.path.abspath (__file__)))


def brrow_moeny (add_count_id, borrowing_moeny, brrowing_yuefen):
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
			dump_account (account_data)
			print (f"借款成功,你已成功借款{account_data ['jiekuan_money']}元，还款日期是{account_data ['jiekuan_date']}")
	else:
		print ('借款失败,原因未知')


"判断是否是还款期预期"


def judge_money_date ():
	now_time = datetime.datetime.today ().date ()
	for (dirpath, dirnames, filenames) in walk (f'{BASE_DIR}/db/accounts'):
		for file in filenames:
			if file.endswith ('json'):
				db_path = db_handle.db_handle (settings.DATABASE)
				account_file = f"{db_path}/{file}"
				with open (account_file, 'r') as f:
					account_data = json.load (f)
					if str (now_time) >= account_data ['jiekuan_date'] != 0:
						print (
							f"账户{file[:-5]}没有进行即使还款，还款金额{account_data['jiekuan_money']},最后还款日期为{account_data['jiekuan_date']},请注意及时催交\n")


if __name__ == '__main__':
	judge_money_date ()  # brrow_moeny(123456,100,2)
