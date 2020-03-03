#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import datetime
import os


def SaveWord(word, data_file):
    path = os.getcwd() + r'\result_files\word_files\{}'.format(datetime.datetime.now().strftime('%Y - %m-%d'))
    if not os.path.exists(path):
        os.makedirs(path)
    word.save(path + r'\{}-{}.docx'.format(data_file, datetime.datetime.now().strftime('%H%M%S')))
