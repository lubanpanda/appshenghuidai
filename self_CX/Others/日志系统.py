#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import logging


def initLogging (logFilename):
	"""Init for logging
	"""
	logging.basicConfig (level = logging.DEBUG, format = '%(asctime)s-%(levelname)s-%(message)s',
	                     datefmt = '%y-%m-%d %H:%M', filename = logFilename, filemode = 'a+')
	console = logging.StreamHandler ()
	console.setLevel (logging.DEBUG)
	formatter = logging.Formatter ('%(asctime)s-%(levelname)s-%(message)s')
	console.setFormatter (formatter)
	logging.getLogger ('').addHandler (console)


initLogging ('a.log')
