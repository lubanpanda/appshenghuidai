#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

class LogPO():
    def __init__(self, locate):
        self.__locate = locate
        self.__cont = None
        self.__tab6 = None

    def LogPOinitControl(self, upwin):
        for i in range(len(self.__locate)):
            tab2 = self.__locate[i][1]
            tabcontrol, names = tab2.split(":")
            if i == 0:
                self.__cont = upwin.DocumentControl(ClassName=names)
            elif i == 1:
                self.__tab6 = upwin.TabControl(AutomationId=names)

    def getcont(self):
        return self.__cont

    def getTab6(self):
        return self.__tab6
