#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import os
from os import walk


def installAllApks (dir = './'):
	for (dirpath, dirnames, filenames) in walk (dir):  # 第一个起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。
		for file in filenames:
			if file.endswith ('.apk'):
				installApk (file)


def installApk (file):
	if os.system ("adb install " + file) != 0:
		exit ('error')
		print ('instatll ' + file + ' success')


if __name__ == '__main__':
	installAllApks ()
