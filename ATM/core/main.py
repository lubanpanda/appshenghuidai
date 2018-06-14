#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda

from ATM.core import auth
from ATM.core.accounts import load_current_balane, loads_current_balane
from ATM.core.transaction import mak_transaction, mak_reimbursement
from ATM.log.atm_log import *


#临时的账户数据记录
user_data={
	'account_id':None,#账户的名字
	'is_authenticated':False,#验证是否通过，通过后为TRUE
	'account_data':None #账户详情
}
def account_info(acc_data=user_data['account_data']):

	log().info(f"-------你的账户信息如下---------\,账户:{acc_data['account_id']},密码:{acc_data['account_data']['password']},总资产:{acc_data['account_data']['balance']},利息:{acc_data['account_data']['interest']},卡的有效期:{acc_data['account_data']['expire_date']}")
	print("请问是否还需要其他服务，是的话请选择服务菜单")
	interactive(acc_data)

def interactive(acc_data):
	menu='''
	---------welcome to panda bank----------
	1.账户信息
	2.还款功能
	3.存款功能
	4.转账
	5.账单
	6.退出
	
	'''
	menu_dic={
		'1':account_info,
		'2':repay,
		'3':withdrae,
		'4':transfer,
		'5':pay_check,
		'6':logout
	}

	exit_flag=False
	if not exit_flag:
		print(menu)
		user_option=input(">>>".strip())

		if user_option in menu_dic:
			menu_dic[user_option](acc_data)

		else:
			print('输入的序号错误，请重新输入')

def withdrae(acc_data):
	account_data=load_current_balane(acc_data['account_id'])
	# print(account_data)
	infp=f"""
	---------欢迎使用panda银行系统-----------
	你的信用值是：{account_data['credit']}
	你的可取款金额是：{account_data['balance']}
	"""
	print(infp)
	back_flag=False
	if not back_flag:
		qukuan_money=input("请输入你要存款的金额或者输入0选择退出进行其他操作:").strip()
		if len(qukuan_money)>0 and qukuan_money.isdigit():
			new_balance=mak_transaction(account_data,'repay',qukuan_money)
			if new_balance:
				print("存款成功")
			interactive(acc_data)
		else:
			print("你输入的金额有误，请重新输入,或者输入0选择退出进行其他操作")



def logout(acc_data):
	exit()

def pay_check(acc_data):
	pass

def repay(acc_data):
	account_data=load_current_balane(acc_data['account_id'])
	infp=f"""
		---------欢迎使用panda银行系统-----------
		你的信用值是：{account_data['credit']}
		你需要还款金额是：{account_data['repay']}
		"""
	print(infp)
	back_flag=False
	if not back_flag:
		huankuan_money=input("请输入你要存款的金额或者输入0选择退出进行其他操作:").strip()
		if len(huankuan_money)>0 and huankuan_money.isdigit():
			huanqian=account_data['repay']
			if abs(huanqian)>=int(huankuan_money):
				print("还款金额输入正确")
				huanqian += int (huankuan_money)
				account_data['repay']=huanqian
				huankuan_qian = mak_transaction (account_data, 'withdraw', huankuan_money)
				print(f"现在的账户余额还有{huankuan_qian['balance']}")
				if huanqian==0:
					print("你的所有账款已还清")
				else:
					print(f"还有{account_data['repay']}未还")
				interactive(acc_data)

			else:
				print(f"还款金额输入错误或者你已经还清了所有的欠款")
				interactive(acc_data)


def transfer(acc_data):
	account_data = load_current_balane (acc_data ['account_id'])
	infp = f"""
			---------欢迎使用panda银行系统-----------
			你的信用值是：{account_data['credit']}
			你账户金额是：{account_data['balance']}
			"""
	print (infp)
	shoukuan_flag=False
	if not shoukuan_flag:
		shoukuan_id=input('请输入收款方账户的6位id：').strip()
		if shoukuan_id:
			try:
				accounts_data = loads_current_balane (shoukuan_id)
				print(f"现在借款方金额为{accounts_data['balance']}元")
				if len(shoukuan_id)==6 and shoukuan_id.isdigit():
					huankuan_info=mak_reimbursement(account_data,shoukuan_id)
					print("请选择其他服务")
					interactive(acc_data)
			except Exception :
				print("没有此账号，请重新选择服务")
				interactive(acc_data)




def run():
	acc_data=auth.acc_login(user_data)  #判断是否登陆
	if user_data['is_authenticated']:   #如果没有认证就更改下状态
		user_data['account_data']=acc_data
		interactive(user_data)          #与用户的交互