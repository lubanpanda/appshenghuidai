#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import logging


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
    # logging.info("你说")
    # logging.error("没事")
    return logging


##################################################################

from loguru import logger

logger.add("aa.log", encoding='utf-8')
logger.debug('这是一个bug')
logger.info("this is a info message")
logger.error("this is a error message")
logger.warning("this is a warning message")

import socket

hostname = socket.gethostname()
name = socket.gethostbyname(hostname)
print(name)
input('按任意键退出')

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



# initLogging('a.log')
