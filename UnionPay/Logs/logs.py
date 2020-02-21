#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import datetime
import os

import loguru


class Logs():
    def __init__(self):
        self.__logger = loguru.logger

    def Loginit(self):
        a = self.__logger._handlers
        if len(a) == 1:
            self.__logger._handlers.clear()
            paths = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.__logger.add(paths + r"\log\Allfiles\{}.log".format(datetime.datetime.now().strftime('%Y-%m-%d')),
                              encoding='utf-8')

        return self.__logger

    def getLogger(self):
        return self.__logger

    def deleteHand(self):
        return self.__logger.__handlers.clear()
