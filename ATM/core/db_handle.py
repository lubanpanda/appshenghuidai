#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  


def file_db_handle(conn_params):
	"""

	:param conn_params:
	:return:返回账户信息的路径
	"""
	print('file db:',conn_params)
	db_path=f"{conn_params['path']}/{conn_params['name']}"
	return db_path


def db_handle(coon_parms):
	"""

	:param coon_parms:
	:return:验证系统信息
	"""
	if coon_parms['engine']=='file_storage':
		return file_db_handle(coon_parms)