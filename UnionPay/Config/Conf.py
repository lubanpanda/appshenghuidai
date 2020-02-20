#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import configparser
import os


class Conf():
    def __init__(self):
        self.__confPath = None

    def readConf(self, confName):
        conf = configparser.ConfigParser()
        paths = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        conf.read(paths + os.sep + "Config" + os.sep + confName, encoding='utf-8')
        return conf
