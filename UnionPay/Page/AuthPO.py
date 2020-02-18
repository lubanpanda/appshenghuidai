#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"
import uiautomation as upwin


class AuthPO():
    def __init__(self, locate):
        self.__locate = locate
        self.__tab1 = None
        self.__pane1 = None
        self.__list1 = None
        self.__tree1 = None
        self.__button = None

    def initControl(self):
        for i in range(len(self.__locate)):
            tab1 = self.__locate[i][1]
            tabcontrol, name = tab1.split(":")
            if i == 0:
                self.__tab1 = upwin.TabItemControl
