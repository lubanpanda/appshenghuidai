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




# initLogging('a.log')
