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