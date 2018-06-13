#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  


def file_db_handle(conn_params):
	print('file db:',conn_params)
	db_path=f"{conn_params['path']}/{conn_params['name']}"
	return db_path


def db_handle(coon_parms):
	if coon_parms['engine']=='file_storage':
		return file_db_handle(coon_parms)