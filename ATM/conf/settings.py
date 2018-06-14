#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE={
	'engine':'file_storage',
	'name':'accounts',
	'path':f'{BASE_DIR}/db'
}

TRANSACTION_TYPE={
	'repay':{'action':'plus','interest':0},#还款
	'withdraw': {'action': 'minus', 'interest': 0.05},#取钱
	'transfer': {'action': 'minus', 'interest': 0.05},#转账
	'consume': {'action': 'minus', 'interest': 0},#刷卡

}