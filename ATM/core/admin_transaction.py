#!/usr/bin/env python3
# -*- coding: utf-8 -*

__author__ = "panda  84305510@qq.com"

from ATM.conf import settings
from ATM.core import db_handle
import os
import json
from ATM.core.accounts import dump_account


"""
主要做一些关于admin的一些操作信息

"""
def modify_password(admin_id):
	db_path = db_handle.db_handle (settings.DATABASE)
	account_file = f"{db_path}/{admin_id}.json"
	if os.path.isfile(account_file):
		with open(account_file,'r') as f:
			account_data=json.load(f)
			true_password = input(f"你当前的密码为{account_data['password']}，是否进行修改，修改输入Y不修改输入N")
			if true_password=='Y':
				pass_id=3
				while True:
					trues_password=input('请输入修改后的密码')
					truse_too_password=input("请在输入一次密码")
					if trues_password==truse_too_password:
						print('密码修改成功')
						account_data["password"]=trues_password
						dump_account(account_data)
						break
					else:
						pass_id -= 1
						if pass_id==0:
							print('你已经没有修改密码的机会了')
							break
						else:
							print (f'两次输入的密码不一致，请重新输入,还有{pass_id-1}次机会')
							continue
			elif true_password=='N':
				print('你取消了本次密码的修改')
			else:
				print('输入有误，已退出修改密码功能')

	else:
		print('你输入的账户有误,请核对后重新输入')


def freeze_account(admin_id):
	db_path = db_handle.db_handle (settings.DATABASE)
	account_file = f"{db_path}/{admin_id}.json"
	if os.path.isfile (account_file) and admin_id!='admin':
		with open (account_file, 'r') as f:
			account_data = json.load (f)
			account_data['Lock_the_card']='True'
			dump_account(account_data)
			print(f'冻结{admin_id}账户成功')
	else:
		print('没有此账户或不能冻结管理员账户')

def add_account_vip(add_count_id):
	db_path = db_handle.db_handle (settings.DATABASE)
	account_file = f"{db_path}/{add_count_id}.json"
	if os.path.isfile (account_file) and add_count_id!='admin':
		with open (account_file, 'r') as f:
			account_data = json.load (f)
			account_data['VIP']='True'
			account_data['vip_level']=1
			dump_account(account_data)
			print('开通VIP账户成功')

	else:
		print('没有此账户或管理员账户不能设置为VIP')
if __name__ == '__main__':
	add_account_vip(123456)