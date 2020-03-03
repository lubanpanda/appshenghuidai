#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser

class Conf():
    def __init__(self):
        self.__confPath = None

    def readConf(self, confName):
        conf = configparser.ConfigParser()
        conf.read(confName, encoding='utf-8')

        return conf


if __name__ == '__main__':
    a = Conf()
    print(a.readConf("configone.ini"))
