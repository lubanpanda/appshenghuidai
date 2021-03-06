#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import json

from ATM.conf import settings
from ATM.core import db_handle


def admin_lock (accounts_data, account_id):
	db_path = db_handle.admins_db_handle (settings.ADMIN_DATABASE)
	account_file = f"{db_path}/{account_id}.json"
	with open (account_file, 'w') as f:
		acc_data = json.dump (accounts_data, f)
		return acc_data

def load_current_balane (account_id):
	"""
	:param account_id:用户名
	:return:
	"""
	db_path = db_handle.db_handle (settings.DATABASE)
	account_file = f"{db_path}/{account_id}.json"
	with open (account_file) as f:
		acc_data = json.load (f)
		return acc_data


def loads_current_balane (account_id):
	"""
	:param account_id:用户名
	:return:
	"""
	db_path = db_handle.too_db_handle (settings.DATABASE)
	account_file = f"{db_path}/{account_id}.json"
	with open (account_file) as f:
		acc_data = json.load (f)
		return acc_data


def dump_account (account_data):
	"""
	:param account_data:用户总信息
	:return:
	"""
	db_path = db_handle.db_handle (settings.DATABASE)
	account_file = f"{db_path}/{account_data['id']}.json"
	with open (account_file, 'w') as f:
		acc_data = json.dump (account_data, f)
		return acc_data


def dumps_account (accounts_data):
	db_path = db_handle.too_db_handle (settings.DATABASE)
	account_file = f"{db_path}/{accounts_data['id']}.json"
	with open (account_file, 'w') as f:
		acc_data = json.dump (accounts_data, f)
		return acc_data


def save_red_info (accounts_data, names):
	"""

	:param accounts_data:
	:param names:抢红包的名字
	:return:
	"""
	dbs_path = db_handle.red_path (settings.DATABASE)
	account_file = f"{dbs_path}{names}.txt"
	with open (account_file, 'a+') as f:
		acc_data = f.write (accounts_data)
		return acc_data


def Open_account (admin_id, info_account):
	"""

	:param admin_id:开户ID
	:param info_account: 开户的信息
	:return:
	"""
	dbs_path = db_handle.db_handle (settings.DATABASE)
	account_file = f"{dbs_path}/{admin_id}.json"
	with open (account_file, 'w') as f:
		acc_data = f.write (json.dumps (info_account))
	return acc_data