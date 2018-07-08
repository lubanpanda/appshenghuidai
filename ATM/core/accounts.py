#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda
from ATM.conf import settings
from ATM.core import db_handle
import json


def load_current_balane(account_id):
	"""

	:param account_id:用户名
	:return:
	"""
	db_path = db_handle.db_handle (settings.DATABASE)
	account_file = f"{db_path}/{account_id}.json"
	with open(account_file) as f:
		acc_data=json.load(f)
		return acc_data

def loads_current_balane(account_id):
	"""

	:param account_id:用户名
	:return:
	"""
	db_path = db_handle.too_db_handle(settings.DATABASE)
	account_file = f"{db_path}/{account_id}.json"
	with open(account_file) as f:
		acc_data=json.load(f)
		return acc_data

def dump_account(account_data):
	"""

	:param account_data:用户总信息
	:return:
	"""
	db_path = db_handle.db_handle (settings.DATABASE)
	account_file = f"{db_path}/{account_data['id']}.json"
	with open (account_file,'w') as f:
		acc_data=json.dump(account_data,f)
		return  True

def dumps_account(accounts_data):
	db_path = db_handle.too_db_handle (settings.DATABASE)
	account_file = f"{db_path}/{accounts_data['id']}.json"
	with open (account_file, 'w') as f:
		acc_data = json.dump (accounts_data, f)
		return True

def save_red_info(accounts_data,names):
	dbs_path=db_handle.red_path(settings.DATABASE)
	account_file=f"{dbs_path}{names}.txt"
	with open(account_file,'a+') as f:
		acc_data=f.write(accounts_data)
		return True
if __name__ == '__main__':
	# load_current_balane('123456')
    dump_account('123456')