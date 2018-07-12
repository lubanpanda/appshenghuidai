#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  


import logging.config


def log ():
	logging.config.fileConfig ("../log/config.conf")
	logging.getLogger ("denglu")
	return logging


if __name__ == '__main__':
	log ()
