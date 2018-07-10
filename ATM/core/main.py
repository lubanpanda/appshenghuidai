#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

from ATM.core import auth
from ATM.core.accounts import *
from ATM.core.transaction import *
from ATM.core import admin_transaction

#临时的账户数据记录
user_data={
	'account_id':None,#账户的名字
	'is_authenticated':False,#验证是否通过，通过后为TRUE
	'account_data':None #账户详情
}

"管理员的临时数据"
user_Data={
	"admin_id":None,
	'admin_is_authenticated':False,
	'admin_data':None
}

def account_info(acc_data=user_data['account_data']):

	print(f"-------你的账户信息如下---------\n账户:{acc_data['account_id']}\n密码:{acc_data['account_data']['password']}\n总资产:{acc_data['account_data']['balance']}\n利息:{acc_data['account_data']['interest']}\n卡的有效期:{acc_data['account_data']['expire_date']}\n")
	print("请问是否还需要其他服务，是的话请选择服务菜单")
	interactive(acc_data)

def admin_interactive(admin_data):
	menus="""
	----------welcome to admin system----------
	|   1.开户                                 |
	|   2.销户                                 |
	|   3.业务办理                              |
	|   4.退出|                                |
	-------------------------------------------
	
	"""
	menus_dic={
		'1':Open_an_account,
		'2':Pin_households,
		'3':Business_is_dealt,
		'4':admin_logout
	}
	exit_flag = False
	if not exit_flag:
		print (menus)
		user_option = input (">>>".strip ())

		if user_option in menus_dic:
			menus_dic [user_option] (admin_data)

		else:
			print ('输入的序号错误，请重新输入')

def Open_an_account(admin_data):
	pass

def Pin_households(admin_data):
	pass

def Business_is_dealt(admin_data):
	print(admin_data)
	account_data=load_current_balane(admin_data['admin_id'])
	print(account_data)
	input_admin_id = input ('--------亲爱的用户，请选择你要办理的业务----------\n1.修改用户交易密码\n2.冻结账户\n\n')
	shuru_id=1
	while shuru_id<=3:
		if input_admin_id==str(1):
			shuru_xiugai_id=input('请输入要修改的账户ID')
			admin_transaction.modify_password(shuru_xiugai_id)
			admin_interactive(account_data)
		elif input_admin_id==str(2):
			pass

		else:
			print("输入有误，请重新输入")
			shuru_id+=1
	print('你输入的指令次数错误太多，已经暂停服务，如需服务请重新开始操作')



	pass
def interactive(acc_data):
	menu='''
	|--------welcome to panda bank--------- |
	|	1.账户信息                           |
	|	2.还款功能                           |
	|	3.存款功能                           |
	|	4.转账                               |
	|	5.发红包                             |
	|	6.退出                               |
	|----------------------------------------
	'''
	menu_dic={
		'1':account_info,
		'2':repay,
		'3':withdrae,
		'4':transfer,
		'6':logout,
		'5':Send_a_red
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


def Send_a_red(acc_data):
	account_data=load_current_balane(acc_data['account_id'])    #获取登陆人的信息
	print(f"#######欢迎来到银行发红包系统，目前你的金额为{account_data['balance']}元#######")
	hongbao_flag=False
	if not hongbao_flag:
		send_grad=input('请输入你要发送红包的金额，最低为0元，最高为200元:'+os.linesep).strip()
		if len(send_grad)>0 and send_grad.isdigit():
			if str(0) < send_grad <= str(200):
				grad_number=input('请输入红包个数').strip()
				numbers=1
				if str(0) >= grad_number > str(send_grad * 100):
					print('红包输入的个数有误')
					numbers+=0
					if numbers==3:
						print('输入次数太多，已退出红包程序')
						interactive(acc_data)
				else:
					print('红包发送成功')
					Save_gade_money(account_data,send_grad)
					print(f'哇，有人发{send_grad}红包了，大家快来抢吧')
					qiang_red(int(send_grad),int(grad_number))
			else:
				print('你输入的金额有误')
				Send_a_red(acc_data)
		return send_grad


def admin_logout(admin_data):
	exit()

def logout(acc_data):
	account_data=load_current_balane(acc_data['account_id'])
	print(f"账户{account_data['id']}已退出")
	exit()


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


def ordinary_user():
	acc_data = auth.acc_login (user_data)  # 判断是否登陆
	if user_data ['is_authenticated']:  # 如果没有认证就更改下状态
		user_data ['account_data'] = acc_data
		interactive (user_data)  # 与用户的交互

def administrator():
	acc_data=auth.admin_login(user_Data)
	if user_Data['admin_is_authenticated']:
		user_Data['admin_data']=acc_data
	print('登陆成功啦～～～～～～～～～')
	admin_interactive (user_Data)

def run():
	input_id=input('请选择你要登陆的账户类型，1是管理员用户，2是普通账户,其余任意键退出\n')
	if input_id==str(1):
		administrator()
	elif input_id==str(2):
		ordinary_user()
	else:
		print("欢迎你下次使用本银行")
		exit()