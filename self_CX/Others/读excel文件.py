#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import os

import demjson
import phone
import requests
import xlrd
import xlwt

DIR_ir = os.path.dirname (os.path.dirname (os.path.abspath (__file__)))


def select_phone_addr (addrs):
	data = xlrd.open_workbook (addrs)
	a = data.sheet_names ()
	table_one = data.sheet_by_name (a [0])
	bb = table_one.nrows
	book = xlwt.Workbook (encoding = 'utf-8')
	book_info = book.add_sheet (a [0], cell_overwrite_ok = True)
	a_id = 0
	for i in range (bb):
		rows = table_one.row_values (i)
		phone_id = rows [0] + '0001'
		aaa = phone.Phone ().find (phone_id)
		if aaa is None:
			# book_info.write(i,0,rows)
			# book_info.write(i,1,'查询不到归属地')
			# book_info.write(i,2,'查询不到运营商')
			url = f'http://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel={phone_id}'
			response = requests.get (url)
			# print(response.text)
			# 归属地
			# print(response.text[54:-109])
			book_info.write (i, 0, rows)
			book_info.write (i, 1, response.text [52:-102])
			book_info.write (i, 2, response.text [70:-82])
			a_id += 1
		else:
			book_info.write (i, 0, rows)
			demjson.encode (aaa)
			ccc = aaa ['province'] + "-" + aaa ['city']
			book_info.write (i, 1, ccc)
			book_info.write (i, 2, aaa ['phone_type'])
	book.save (DIR_ir + '/phones.xls')


if __name__ == '__main__':
	select_phone_addr ("/Users/yuchengtao/Downloads/phones.xlsx")
