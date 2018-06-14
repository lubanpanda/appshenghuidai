#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
import os
import time
import json
from ATM.conf import settings
from ATM.core import db_handle
from ATM.log.atm_log import *


def acc_auch(accout, password):
	"""
	:param accout: 账户
	:param password: 登陆密码
	:return:
	"""
	#返回当前的路径信息，通过配置信息来验证是否正确
	db_path=db_handle.db_handle(settings.DATABASE)
	account_file= f"{db_path}/{accout}.json"
	print(account_file)
	if os.path.isfile(account_file):
		with open(account_file,'r') as f:
			account_data=json.load(f)
			if account_data['password']==password:
				exp_time_stamp=time.mktime(time.strptime(account_data['expire_date'],"%Y-%m-%d"))
				if time.time()>exp_time_stamp:
					print('你的账户已经过期')
				else:
					return account_data
			else:
				print('你输入的密码不正确')
	else:
		print('没有这个文件目录')


def acc_login(user_data):
	"""

	:param user_data:是否已经认证
	:return:
	"""
	retry_count=0
	while user_data['is_authenticated'] is not True and retry_count<3:
		accout=input('请输入你的账号'.strip()+os.linesep)
		password=input('请输入你的密码'.strip()+os.linesep)
		auch=acc_auch(accout,password)
		if auch:
			user_data['is_authenticated']=True
			user_data['account_id']=accout
			return auch
		retry_count+=1
	else:
		logging.info(f"输入的账号{accout}太多")
		exit()




































