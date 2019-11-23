#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import logging


# python自带的日志模块
def Loggings():
    """Init for logging
    """
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s',
                        datefmt='%y-%m-%d %H:%M:%S', filename="a.log", filemode='a+')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    return logging


##################################################################
# 第三方日志模块，语法简单
from loguru import logger

logger.add('runtime_{time}.log', rotation='00:00', encoding='utf-8')
logger.debug('这是一个bug')
logger.info("this is a info message")
logger.error("this is a error message")
logger.warning("this is a warning message")


from logzero import logger

# import uiautomation
# These log messages are sent to the console
logger.debug("这是一个程序")
logger.info("读取了一条数据")
logger.warning("此数据可能有异常")
logger.error("保存按钮没有找到")

from logbook import Logger, StreamHandler, TimedRotatingFileHandler
import sys
import os

StreamHandler(sys.stdout).push_application()
log = Logger('Logbook')
log.info('Hello, World!')
LOG_DIR = os.path.join('log')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
TimedRotatingFileHandler(os.path.join(LOG_DIR, '%s.log' % 'user_log'), date_format='%Y%m%d',
                         bubble=True).push_application()
user_log = Logger('user_log')
user_log.info('user_log mytest....')