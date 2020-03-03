#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import os


def SaveCaseLog(co_name, complete_content):
    file_name = co_name.replace('/', '-') + ".txt"
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    paths = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = paths + r'\result_files\case_log_files\{}'.format(today)
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = path + r'\{}'.format(file_name)
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(complete_content)
