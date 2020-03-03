#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import os

import loguru


class Logs():
    def __init__(self):
        self.__logger = loguru.logger

    def Loginit(self):
        self.__logger.remove(handler_id=None)
        self.__logger.add(os.getcwd() + r"\log\Allfiles\{}.log".format(datetime.datetime.now().strftime('%Y-%m-%d')),
                          encoding='utf-8')
        return self.__logger

    def getLogger(self):
        return self.__logger


if __name__ == '__main__':
    a = Logs()
    a.Loginit()
