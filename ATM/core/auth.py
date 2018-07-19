#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import json
import os
import time

from ATM.conf import settings
from ATM.core import db_handle
from ATM.core.accounts import dump_account
from ATM.log.atm_log import *


def acc_auch (accout, password, pass_word):
	"""
	:param accout: 账户
	:param password: 登陆密码
	:param pass_word:次数的判定
	:return:
	"""
	# 返回当前的路径信息，通过配置信息来验证是否正确
	db_path = db_handle.db_handle (settings.DATABASE)
	account_file = f"{db_path}/{accout}.json"
	if os.path.isfile (account_file):
		with open (account_file, 'r') as f:
			account_data = json.load (f)
			try:
				if account_data ["Lock_the_card"] == '':
					if account_data ['password'] == password:
						exp_time_stamp = time.mktime (time.strptime (account_data ['expire_date'], "%Y-%m-%d"))
						if time.time () > exp_time_stamp:
							print ('你的账户已经过期,请重新补办新的银行卡或重新登陆')
						else:
							return account_data
					else:
						print ('你输入的密码不正确')
						pass_word += 1
						if pass_word == 3:
							print ('卡的密码输入次数过多，卡已经被锁定,请联系银行工作人员进行解锁')
							account_data ["Lock_the_card"] = 'True'
							dump_account (account_data)
							exit ()
				elif account_data ["Lock_the_card"] == 'True':
					print ('你的卡已经被锁定不能进行操作了，请联系银行工作人员')
					exit ()
			except Exception:
				print ('没有这个账号')
	else:
		print ('没有这个账户目录')


def admin_acc_auch (admin_id, admin_password):
	"""

	:param admin_id:管理员账户
	:param admin_password:管理员密码
	:return:
	"""
	db_path = db_handle.admins_db_handle (settings.ADMIN_DATABASE)
	account_file = f"{db_path}.json"
	pass_word = 1
	if os.path.isfile (account_file):
		with open (account_file, 'r') as f:
			account_data = json.load (f)
			try:
				if account_data ['admin_id'] == admin_id:
					if account_data ['admin_password'] == admin_password:
						return account_data
					else:
						print ('你输入的密码不正确')
						pass_word += 1
						if pass_word == 3:
							print ('卡的密码输入次数过多，请稍后再来尝试')
				else:
					print ('没有这个账户')
			except:
				pass


def acc_login (user_data):
	"""
	:param user_data:是否已经认证
	:return:
	"""
	retry_count = 0
	while user_data ['is_authenticated'] is not True and retry_count < 3:
		accout = input ('请输入你的账号'.strip () + os.linesep)
		password = input ('请输入你的密码'.strip () + os.linesep)
		# accout = '123456'
		# password = '111'
		auch = acc_auch (accout, password, retry_count)
		if auch:
			user_data ['is_authenticated'] = True
			user_data ['account_id'] = accout
			return auch
		retry_count += 1
	else:
		logging.info (f"你的账号已经通过了认证权限")
		exit ()


def admin_login (user_Data):
	"""

	:param user_Data:账户信息
	:return:
	"""
	admin_count = 0
	while user_Data ['admin_is_authenticated'] is not True and admin_count < 3:
		admin_accout = input ('请输入你的账号'.strip () + os.linesep)
		admin_password = input ('请输入你的密码'.strip () + os.linesep)
		# admin_accout='admin'
		# admin_password='123456'
		auchs = admin_acc_auch (admin_accout, admin_password)
		if auchs:
			user_Data ['admin_is_authenticated'] = True
			user_Data ['admin_id'] = admin_accout
			return auchs
		admin_count += 1
	else:
		logging.info (f"你的账号已经通过了认证权限")
		exit ()
