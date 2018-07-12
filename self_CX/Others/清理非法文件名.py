#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/5/26 下午10:57
# @Author  : Panda
import os

from pip._vendor import chardet


def file_name_is_legal (name):
	detect = chardet.detect (name.encode ('utf-8'))
	return detect ['encoding'] == 'ascii' or name.endswith ('.py')


def clean_illeage_files (root):
	for path, folders, files in os.walk (root):
		for file in files:
			if not file_name_is_legal (file):
				os.remove (os.path.join (path, file))
				print (file, ' 不合法，已删除')


if __name__ == '__main__':
	clean_illeage_files (os.curdir)
