#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import datetime
import os


def SaveWord(word, data_file):
    paths = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = paths + r'\result_files\word_files\{}'.format(datetime.datetime.now().strftime('%Y - %m-%d'))
    if not os.path.exists(path):
        os.makedirs(path)
    word.save(path + r'\{}-{}.docx'.format(data_file, datetime.datetime.now().strftime('%H%M%S')))
