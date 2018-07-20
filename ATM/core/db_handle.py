#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"


def file_db_handle (conn_params):
	"""
	:param conn_params:
	:return:返回账户信息的路径
	"""
	db_path = f"{conn_params['path']}/{conn_params['name']}"
	return db_path


def db_handle (coon_parms):
	"""
	:param coon_parms:
	:return:验证系统信息
	"""
	if coon_parms ['engine'] == 'file_storage':
		return file_db_handle (coon_parms)


def too_file_db_handles (conn_params):
	"""
	:param conn_params:收款人路径
	:return:
	"""
	db_paths = f"{conn_params['path']}/{conn_params['too_name']}"
	return db_paths


def too_db_handle (conn_params):
	if conn_params ['names'] == 'panda':
		return too_file_db_handles (conn_params)


def red_path (conn_params):
	db_paths = f"{conn_params['red_path']}"
	return db_paths


def admin_db_handle (conn_params):
	db_path = f"{conn_params['path']}"
	return db_path


def admins_db_handle (conn_params):
	if conn_params ['names'] == 'admin':
		return admin_db_handle (conn_params)
