#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  84305510@qq.com

import logging.config
def log():
    logging.config.fileConfig ("../panda_log/config.conf")
    logging.getLogger ("example01")
    return logging

if __name__ == '__main__':
    log()