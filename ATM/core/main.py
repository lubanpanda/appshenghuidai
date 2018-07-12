#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

from ATM.core import auth
from ATM.core.accounts import *
from ATM.core.transaction import *
from ATM.core import admin_transaction


############################账户信息模块########################
#临时的账户数据记录
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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



####################管理员账户操作#######################

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
	|   4.退出                                 |
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
	account_data=load_current_balane(admin_data['admin_id'])
	account_id=input('请输入账户ID:')
	account_password=input('请输入密码:')
	for (dirpath, dirnames, filenames) in os.walk (f'{BASE_DIR}/db/accounts'):
		for file in filenames:
			if account_id=='admin' or account_id+'.json'==file:
				print('不能创建管理员账号或已经存在的账户')
				admin_interactive(admin_data)
			else:
				cunkuan_json={
					"id": account_id,
					"repay": 0,
					"status": 0,
					"password": account_password,
					"pay_dat": 0,
					"credit": 0,
					"balance": 0,
					"interest": 0,
					"expire_date": "2020-01-01",
					"Lock_the_card": ""

				}
				Open_account(account_id,cunkuan_json)
	print ('开户账户成功,请在选择其他的服务')
	admin_interactive(admin_data)

def Pin_households(admin_data):
	account_list=[]
	account_data = load_current_balane (admin_data ['admin_id'])
	account_id = input ('请输入要销户的账户ID:')
	for (dirpath, dirnames, filenames) in os.walk (f'{BASE_DIR}/db/accounts'):
		for file in filenames:
			account_list.append(file)
	if account_id+'.json' in account_list:
		os.remove(f'{BASE_DIR}/db/accounts/{account_id}.json')
		print('销户成功')
		admin_interactive(admin_data)
	else:
		print(f'{account_id}账户没有找到')
		admin_interactive(admin_data)
def Business_is_dealt(admin_data):
	account_data=load_current_balane(admin_data['admin_id'])
	input_admin_id = input ('--------亲爱的用户，请选择你要办理的业务----------\n1.修改用户交易密码\n2.冻结账户\n3.开通账户会员\n')
	shuru_id=1
	while shuru_id<=3:
		if input_admin_id==str(1):
			shuru_xiugai_id=input('请输入要修改的账户ID：')
			admin_transaction.modify_password(shuru_xiugai_id)
			admin_interactive(account_data)
		elif input_admin_id==str(2):
			freeze_id=input('请输入冻结账户的id')
			admin_transaction.freeze_account(freeze_id)
			admin_interactive(account_data)

		elif input_admin_id==str(3):
			"增加服务字段,往用户里增加一些别的信息，如:是否可以升级为会员"
			add_account_id=input('请输入要添加功能的账号：')
			admin_transaction.add_account_vip(add_account_id)
			admin_interactive(admin_data)
		else:
			print("输入有误，请重新输入")
			shuru_id+=1
	print('你输入的指令次数错误太多，已经暂停服务，如需服务请重新开始操作')



def admin_logout(admin_data):
	exit()

###################普通用户操作#########################

def interactive(acc_data):
	menu='''
	|--------welcome to panda bank--------- |
	|	1.账户信息                           |
	|	2.还款功能                           |
	|	3.存款功能                           |
	|	4.转账                               |
	|	5.发红包
	    6.网上买菜系统                         |
	|	7.退出                               |
	|----------------------------------------
	'''
	menu_dic={
		'1':account_info,
		'2':repay,
		'3':withdrae,
		'4':transfer,
		'5':Send_a_red ,
		'6':Buy_shopping,
		'7': logout,

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

def Buy_shopping(acc_data):
	account_data=load_current_balane(acc_data['account_id'])
	True_or_False=account_data['VIP']
	VIP_LEVEL=account_data['vip_level']
	all_money = 0
	all_moneys=[]
	if True_or_False=='True':
		dazhe=settings.BUSINESS['vip_level']['1']['discount']
		print(f"你是尊贵的VIP{VIP_LEVEL}客户买菜可以打折{dazhe}哦")


		for i in range(len(settings.shucai_menus)):
			aa=settings.shucai_menus[f'{i+1}']["action"]
			bb=settings.shucai_menus[f'{i+1}']["interest"]
			print(i+1,aa,":",bb,"元")

		while True:
			xuanze_id = input ('请选购你的商品，每次的价格都不一样哦')
			danjia_money = settings.shucai_menus [xuanze_id] ["interest"]
			if all_money<account_data['balance']:
				all_moneys.append(danjia_money)
				all_money=all_money+danjia_money
				shiji_money = all_money * dazhe
				shuru_info=input('输入任意键继续,结束购物请按Q')
				if shuru_info=='Q':
					break
				else:
					continue
			else:
				print('你的账户余额不足，请及时充值')
				break
		print('你一共话费了%s元'%shiji_money)
		account_data['balance']=account_data['balance']-shiji_money
		dump_account(account_data)


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

##############登陆的一些交互和方法#################

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