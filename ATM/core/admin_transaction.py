#!/usr/bin/env python3
# -*- coding: utf-8 -*

__author__ = "panda  84305510@qq.com"

import json
import os

from ATM.conf import settings
from ATM.core import db_handle
from ATM.core.accounts import dump_account

"""
主要做一些关于admin的一些操作信息

"""


def modify_password (admin_id):
	"""

	:param admin_id:管理员ID
	:return:
	"""
	db_path = db_handle.db_handle (settings.DATABASE)
	account_file = f"{db_path}/{admin_id}.json"
	if os.path.isfile (account_file):
		with open (account_file) as f:
			account_data = json.load (f)
			true_password = input (f"你当前的密码为{account_data['password']}，是否进行修改，修改输入Y不修改输入N").strip ()
			if true_password == 'Y':
				pass_id = 3
				while True:
					trues_password = input ('请输入修改后的密码').strip ()
					truse_too_password = input ("请在输入一次密码").strip ()
					if trues_password == truse_too_password:
						print ('密码修改成功')
						account_data ["password"] = trues_password
						dump_account (account_data)
						break
					else:
						pass_id -= 1
						if pass_id == 0:
							print ('你已经没有修改密码的机会了')
							break
						else:
							print (f'两次输入的密码不一致，请重新输入,还有{pass_id-1}次机会')
							continue
			elif true_password == 'N':
				print ('你取消了本次密码的修改')
			else:
				print ('输入有误，已退出修改密码功能')
	else:
		print ('你输入的账户有误,请核对后重新输入')


def freeze_account (admin_id, dongjie):
	"""

	:param admin_id:管理员ID
	:param dongjie: 判断状态
	:return:
	"""
	db_path = db_handle.db_handle (settings.DATABASE)
	account_file = f"{db_path}/{admin_id}.json"
	if os.path.isfile (account_file) and admin_id != 'admin':
		with open (account_file) as f:
			account_data = json.load (f)
			if account_data ['Lock_the_card'] == 'True':
				if dongjie == 'False':
					account_data ['Lock_the_card'] = ''
					dump_account (account_data)
					print (f'解冻{admin_id}账户成功')
				else:
					print ('此账户已经被冻结')
			elif account_data ['Lock_the_card'] == '':
				if dongjie == 'True':
					account_data ['Lock_the_card'] = 'True'
					dump_account (account_data)
					print (f'冻结{admin_id}账户成功')
				else:
					print ('此账户没有被冻结')
	else:
		print ('没有此账户或不能冻结管理员账户')


def add_account_vip (add_count_id):
	"""

	:param add_count_id:添加账户的ID
	:return:
	"""
	db_path = db_handle.db_handle (settings.DATABASE)
	account_file = f"{db_path}/{add_count_id}.json"
	if os.path.isfile (account_file) and add_count_id != 'admin':
		with open (account_file) as f:
			account_data = json.load (f)
			if account_data ['VIP'] == 'True':
				print ('此账户已经是VIP了无需重复开通')
			else:
				account_data ['VIP'] = 'True'
				account_data ['vip_level'] = "1"
				dump_account (account_data)
				print ('开通VIP账户成功')

	else:
		print ('没有此账户或管理员账户不能设置为VIP')


def buy_shopping (account_data, True_or_False, VIP_LEVEL):
	"""

	:param account_data:账户信息
	:param True_or_False: 判断是否是VIP
	:param VIP_LEVEL: VIP的级别
	:return:
	"""
	global shiji_money
	all_money = 0
	all_moneys = []
	if True_or_False == 'True':
		dazhe = settings.BUSINESS ['vip_level'] [VIP_LEVEL] ['discount']
		print (f"你是尊贵的VIP{VIP_LEVEL}客户买菜可以打折{dazhe}哦")
		for i in range (len (settings.shucai_menus)):
			aa = settings.shucai_menus [f'{i+1}'] ["action"]
			bb = settings.shucai_menus [f'{i+1}'] ["interest"]
			print (i + 1, aa, ":", bb, "元")
		while True:
			xuanze_id = input ('请选购你的商品，每次的价格都不一样哦').strip ()
			if xuanze_id.isdigit ():
				danjia_money = settings.shucai_menus [xuanze_id] ["interest"]
				if all_money < account_data ['balance']:
					all_moneys.append (danjia_money)
					all_money = all_money + danjia_money
					shiji_money = all_money * dazhe
					shuru_info = input ('输入任意键继续,结束购物请按Q').strip ()
					if shuru_info == 'Q':
						break
					else:
						continue
				else:
					print ('你的账户余额不足，请及时充值')
					break
			else:
				print ('请输入正确的编号')
				continue
		print ('你一共话费了%s元' % shiji_money)
		account_data ['balance'] = account_data ['balance'] - shiji_money
		account_data ['VIP_jifen'] = round (account_data ['VIP_jifen'] + shiji_money, 2)
		dump_account (account_data)
		VIP_jifen (account_data)


def VIP_jifen (account_data):
	"""

	:param account_data:账户总信息
	:return: 积分的多少来确定VIP的等级
	"""
	if 0 < account_data ['VIP_jifen'] <= 50:
		account_data ['vip_level'] = "1"
	elif 50 < account_data ['VIP_jifen'] <= 100:
		account_data ['vip_level'] = "2"
	elif 100 < account_data ['VIP_jifen'] <= 150:
		account_data ['vip_level'] = "3"
	elif 150 < account_data ['VIP_jifen'] <= 200:
		account_data ['vip_level'] = "4"
	elif 200 < account_data ['VIP_jifen'] < 250:
		account_data ['vip_level'] = "5"
	elif 250 < account_data ['VIP_jifen']:
		account_data ['vip_level'] = "6"
	dump_account (account_data)
	print (f"你的当前VIP等级为{account_data['vip_level']}，积分{account_data['VIP_jifen']}")
