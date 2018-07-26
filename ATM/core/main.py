#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"
__version__ = '1.0.0'

from ATM.core import admin_transaction, auth, borrow_info
from ATM.core.accounts import *
from ATM.core.transaction import *

############################账户信息模块########################
# 临时的账户数据记录
BASE_DIR = os.path.dirname (os.path.dirname (os.path.abspath (__file__)))

user_data = {'account_id': None,  # 账户的名字
             'is_authenticated': False,  # 验证是否通过，通过后为TRUE
             'account_data': None  # 账户详情
             }

"管理员的临时数据"
user_Data = {"admin_id": None, 'admin_is_authenticated': False, 'admin_data': None}


############################管理员账户操作#######################

def account_info (acc_data = user_data ['account_data']):
	print (f"-------你的账户信息如下---------\n"
	       f"账户:{acc_data['account_id']}\n"
	       f"密码:{acc_data['account_data']['password']}\n"
	       f"总资产:{acc_data['account_data']['balance']}\n"
	       f"信用值:{acc_data['account_data']['credit']}\n"
	       f"利息:{acc_data['account_data']['interest']}\n"
	       f"卡的有效期:{acc_data['account_data']['expire_date']}\n"
	       f"会员等级:{acc_data['account_data']['vip_level']}\n"
	       f"借款金额：{acc_data['account_data']['jiekuan_money']}\n"
	       f"还款日期：{acc_data['account_data']['jiekuan_date']}")
	print ("请问是否还需要其他服务，是的话请选择服务菜单")
	interactive (acc_data)


def admin_interactive (admin_data):
	menus = """
	----------welcome to admin system----------
	|   1.开户                                 |
	|   2.销户                                 |
	|   3.业务办理                              |
	|   4.退出                                 |
	-------------------------------------------
	
	"""
	menus_dic = {'1': Open_an_account, '2': Pin_households, '3': Business_is_dealt, '4': admin_logout}
	exit_flag = False
	if not exit_flag:
		print (menus)
		try:
			user_option = input (">>>".strip ())
			if user_option in menus_dic:
				menus_dic [user_option] (admin_data)
			else:
				print ('输入的序号错误，请重新输入')
		except:
			pass


def Open_an_account (admin_data):
	"""
	:param admin_data:
	:return:开户
	"""
	account_id = input ('请输入账户ID:')
	if account_id.isdigit ():
		if 0 < len (account_id) < 6:
			account_password = input ('请输入密码:')
			for (dirpath, dirnames, filenames) in os.walk (f'{BASE_DIR}/db/accounts'):
				for file in filenames:
					if account_id == 'admin' or account_id + '.json' == file:
						print ('不能创建管理员账号或已经存在的账户')
						admin_interactive (admin_data)
					else:
						cunkuan_json = {"id": account_id, "repay": 0, "status": 0, "password": account_password,
						                "pay_dat": 0, "credit": 100, "balance": 0, "interest": 0,
						                "expire_date": "2020-01-01", "Lock_the_card": "", "VIP_jifen": "0",
						                "jiekuan_money": 0, "jiekuan_date": 0

						                }
						Open_account (account_id, cunkuan_json)
			print ('开户账户成功,请在选择其他的服务')
			admin_interactive (admin_data)
		else:
			print ('创建账户的ID不能大于6位')
			admin_interactive (admin_data)
	else:
		print ('你输入的字符非法')
		admin_interactive (admin_data)


def Pin_households (admin_data):
	"""
	:param admin_data:
	:return:销户
	"""
	account_list = []
	account_id = input ('请输入要销户的账户ID:')
	if account_id.isdigit ():
		for (dirpath, dirnames, filenames) in os.walk (f'{BASE_DIR}/db/accounts'):
			for file in filenames:
				account_list.append (file)
		if account_id + '.json' in account_list:
			os.remove (f'{BASE_DIR}/db/accounts/{account_id}.json')
			print ('销户成功')
			admin_interactive (admin_data)
		else:
			print (f'{account_id}账户没有找到')
			admin_interactive (admin_data)
	else:
		print ('你输入的字符非法')
		admin_interactive (admin_data)


def Business_is_dealt (account_data):
	input_admin_id = input ('--------亲爱的用户，请选择你要办理的业务----------\n'
	                        '1.修改用户交易密码\n'
	                        '2.冻结账户\n'
	                        '3.解冻账户\n'
	                        '4.开通账户会员\n'
	                        '请输入办理业务的序号')
	shuru_id = 1
	if input_admin_id.isdigit ():
		while shuru_id <= 3:
			if input_admin_id == str (1):
				shuru_xiugai_id = input ('请输入要修改的账户ID：')
				admin_transaction.modify_password (shuru_xiugai_id)
				admin_interactive (account_data)
			elif input_admin_id == str (2):
				freeze_id = input ('请输入冻结账户的id')
				admin_transaction.freeze_account (freeze_id, 'True')
				admin_interactive (account_data)
			elif input_admin_id == str (3):
				freezes_id = input ('请输入解冻账户的id')
				admin_transaction.freeze_account (freezes_id, 'False')
				admin_interactive (account_data)
			elif input_admin_id == str (4):
				"增加服务字段,往用户里增加一些别的信息，如:是否可以升级为会员"
				add_account_id = input ('请输入要添加功能的账号：')
				admin_transaction.add_account_vip (add_account_id)
				admin_interactive (account_data)
			else:
				print ("输入有误，请重新输入")
				shuru_id += 1
		print ('你输入的指令次数错误太多，已经暂停服务，如需服务请重新开始操作')
	else:
		print ('你输入的字符非法')
		admin_interactive (account_data)


def admin_logout (admin_data):
	exit ()


###################普通用户操作#########################

def interactive (acc_data):
	menu = '''
	**********welcome to panda bank**********
	*	1.账户信息                           *
	*	2.还款功能                           *
	*	3.存款功能                           *
	*   4.转账                               *
	*	5.发红包                             *
	*   6.网上买菜系统                        *
	*   7.贷款业务                           *
	*	8.退出                               *
	*****************************************
	'''
	menu_dic = {'1': account_info, '2': repay, '3': withdrae, '4': transfer, '5': Send_a_red, '6': Buy_shopping,
	            '7': borrowing, '8': logout,

	            }

	exit_flag = False
	if not exit_flag:
		print (menu)
		try:
			user_option = input (">>>".strip ())
			if user_option in menu_dic:
				menu_dic [user_option] (acc_data)
			else:
				print ('输入的序号错误，请重新输入')
				interactive (acc_data)
		except:
			pass


def withdrae (acc_data):
	"""
	:param acc_data:
	:return:存款
	"""
	account_data = load_current_balane (acc_data ['account_id'])
	infp = f"""
	---------欢迎使用panda银行系统-----------
	你的信用值是：{account_data['credit']}
	你现有的金额是：{account_data['balance']}
	"""
	print (infp)
	back_flag = False
	if not back_flag:
		qukuan_money = input ("请输入你要存款的金额或者输入0选择退出进行其他操作:").strip ()
		if qukuan_money.isdigit ():
			if len (qukuan_money) > 0 and qukuan_money.isdigit ():
				new_balance = mak_transaction (account_data, 'repay', qukuan_money)
				if new_balance:
					print ("存款成功")
				interactive (acc_data)
			else:
				print ("你输入的金额有误，请选择进行其他操作内容")
				interactive (acc_data)
		else:
			print ('你输入的字符非法')
			interactive (acc_data)


def Send_a_red (acc_data):
	"""
	:param acc_data:
	:return:发红包
	"""
	account_data = load_current_balane (acc_data ['account_id'])  # 获取登陆人的信息
	print (f"#######欢迎来到银行发红包系统，目前你的金额为{account_data['balance']}元#######")
	hongbao_flag = False
	if not hongbao_flag:
		if account_data ['balance'] > 0:
			send_grad = input ('请输入你要发送红包的金额，最低为0元，最高为200元:' + os.linesep).strip ()
			if send_grad.isdigit ():
				if len (send_grad) > 0 and send_grad.isdigit () and send_grad <= account_data ['balance']:
					if str (0) < send_grad <= str (200):
						grad_number = input ('请输入红包个数').strip ()
						numbers = 1
						if str (0) >= grad_number > str (send_grad * 100):
							print ('红包输入的个数有误')
							numbers += 0
							if numbers == 3:
								print ('输入次数太多，已退出红包程序')
								interactive (acc_data)
						else:
							print ('红包发送成功')
							Save_gade_money (account_data, send_grad)
							print (f'哇，有人发{send_grad}红包了，大家快来抢吧')
							qiang_red (int (send_grad), int (grad_number))
							interactive (account_data)
					else:
						print ('你输入的金额有误')
						Send_a_red (acc_data)
				return send_grad
			else:
				print ('你输入的字符非法')
				interactive (acc_data)


def Buy_shopping (acc_data):
	"""
	:param acc_data:
	:return: 购物
	"""
	account_data = load_current_balane (acc_data ['account_id'])
	True_or_False = account_data ['VIP']
	admin_transaction.VIP_jifen (account_data)
	VIP_LEVEL = account_data ['vip_level']
	admin_transaction.buy_shopping (account_data, True_or_False, VIP_LEVEL)
	dump_account (account_data)
	interactive (acc_data)


def logout (acc_data):
	"""
	:param acc_data:账户的总信息
	:return: 退出程序
	"""
	account_data = load_current_balane (acc_data ['account_id'])
	print (f"账户{account_data['id']}已退出")
	exit ()


def repay (acc_data):
	"""
	:param acc_data:账户的总信息
	:return: 还款
	"""
	account_data = load_current_balane (acc_data ['account_id'])
	infp = f"""
		---------欢迎使用panda银行系统-----------
		你的信用值是：{account_data['credit']}
		你需要还款金额是：{account_data['repay']}
		"""
	print (infp)
	back_flag = False
	if not back_flag:
		huankuan_money = input ("请输入你要还款的金额或者输入0选择退出进行其他操作:").strip ()
		if huankuan_money.isdigit ():
			if len (huankuan_money) > 0 and huankuan_money.isdigit ():
				huanqian = account_data ['repay']
				if abs (huanqian) >= int (huankuan_money):
					print ("还款金额输入正确")
					if huanqian < 0:
						huanqian += int (huankuan_money)  # 还款的钱为负数，所以直接相加即可
						account_data ['repay'] = huanqian
						dump_account (account_data)
						huankuan_qian = mak_transaction (account_data, 'withdraw', huankuan_money)
						print (f"现在的账户余额还有{huankuan_qian['balance']}")
						if huanqian == 0:
							print ("你的所有账款已还清")
						else:
							print (f"还有{account_data['repay']}未还")
						interactive (acc_data)
					else:
						print ('欠债已还清')
				else:
					print (f"还款金额输入错误或者你已经还清了所有的欠款")
					interactive (acc_data)
		else:
			print ('你输入的字符非法')
			interactive (acc_data)


def transfer (acc_data):
	"""
	:param acc_data: 账户的总信息
	:return: 转账
	"""
	account_data = load_current_balane (acc_data ['account_id'])
	infp = f"""
			---------欢迎使用panda银行系统-----------
			你的信用值是：{account_data['credit']}
			你账户金额是：{account_data['balance']}
			"""
	print (infp)
	shoukuan_flag = False
	if not shoukuan_flag:
		shoukuan_id = input ('请输入收款方账户的6位id：').strip ()
		if shoukuan_id and shoukuan_id.isdigit ():
			try:
				accounts_data = loads_current_balane (shoukuan_id)
				print (f"现在借款方金额为{accounts_data['balance']}元")
				if len (shoukuan_id) <= 6 and shoukuan_id.isdigit ():
					mak_reimbursement (account_data, shoukuan_id)
					print ("请选择其他服务")
					interactive (acc_data)
			except Exception:
				print ("没有此账号，请重新选择服务")
				interactive (acc_data)
		else:
			print ('输入的内容非法')
			interactive (acc_data)


def borrowing (acc_data):
	"""
	:param acc_data:账户的总信息
	:return: 借款信息
	"""
	borro_yewu = input ('请输入你要办的的业务：\n1.贷款\n2.还款\n')
	if borro_yewu == str (1):
		account_data = load_current_balane (acc_data ['account_id'])
		print ('信用分低于80时不可以贷款')
		if 80 <= account_data ['credit'] <= 100:
			print ('你的信用积分可以进行贷款')
			borrowing_moeny = input ('请输入你要借贷的金额：')
			brrowing_yuefen = input ('请输入借款的月份,一个月利率为1%，2个月为2%，以此类推')
			if borrowing_moeny.isdigit () and brrowing_yuefen.isdigit ():
				borrow_info.brrow_moeny (account_data ['id'], borrowing_moeny, brrowing_yuefen)
			else:
				print ('有非法字符，请重新操作')
				borrowing (acc_data)
		elif account_data ['credit'] < 80:
			print ('你的信用值太低，不能借款')
		interactive (acc_data)
	elif borro_yewu == str (2):
		account_data = load_current_balane (acc_data ['account_id'])
		print (f"尊敬的{account_data['id']}账户，你目前需要还款的金额是{account_data['jiekuan_money']}元")
		huankuan_money = input ('请输入你要还款的金额：').strip ()
		if huankuan_money.isdigit ():
			huankuan_money = int (huankuan_money)
			borrow_info.reimbursement (account_data ['id'], huankuan_money, account_data ['balance'],
			                           account_data ['jiekuan_money'])
			interactive (acc_data)
		else:
			print ('请输入数字')
			borrowing (acc_data)
	else:
		print ('输入有误')
		interactive (acc_data)



##############登陆的一些交互和方法#################

def ordinary_user ():
	"""
	:return: 账户登陆入口
	"""
	acc_data = auth.acc_login (user_data)  # 判断是否登陆
	if user_data ['is_authenticated']:  # 如果没有认证就更改下状态
		user_data ['account_data'] = acc_data
		interactive (user_data)  # 与用户的交互


def administrator ():
	"""
	:return:管理员登陆入口
	"""
	acc_data = auth.admin_login (user_Data)
	if user_Data ['admin_is_authenticated']:
		user_Data ['admin_data'] = acc_data
	print ('登陆成功啦～～～～～～～～～')
	borrow_info.judge_money_date ()
	admin_interactive (user_Data)


def run ():
	"""
	:return:程序主程序入口
	"""
	try:
		input_id = input ('请选择你要登陆的账户类型，1是管理员用户，2是普通账户,其余任意键退出\n')
		if input_id == str (1):
			administrator ()
		elif input_id == str (2):
			ordinary_user ()
		else:
			print ("欢迎你下次使用本银行")
			exit ()
	except:
		pass
