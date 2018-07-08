#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import os

"""
DATABASE：
模拟数据库的账号做一个拓展，验证信息和用户名，正确后才可以进行转账存款等相应的操作

TRANSACTION_TYPE：
通过设置一个字典直接进行加减的操作(加plus，减minus)，通过判断交易的类型而直接进行运算而不必每次都去做下判断
"""

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE={
	'engine':'file_storage',
	'name':'accounts',
	'names':'panda',
	'too_name':'Paymentaccount',
	'path':f'{BASE_DIR}/db',
	"paths":f"{BASE_DIR}/Paymentaccount",
	"red_path":f"{BASE_DIR}/db/Redenvelopesnatcher/"      #抢红包的名单
}

TRANSACTION_TYPE={
	'repay':{'action':'plus','interest':0},#还款
	'withdraw': {'action': 'minus', 'interest': 0.05},#存钱
	'transfer': {'action': 'minus', 'interest': 0.05},#转账
	'consume': {'action': 'minus', 'interest': 0},#刷卡

}