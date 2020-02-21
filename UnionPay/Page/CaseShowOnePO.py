#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"


class CaseShowOnePO():
    def __init__(self, locate):
        self.__locate = locate
        self.__tab4 = None
        self.__group1 = None

    def CaseShowOneinitControl(self, upwin):
        for i in range(len(self.__locate)):
            tab2 = self.__locate[i][1]
            tabcontrol, names = tab2.split(":")
            if i == 0:
                self.__tab4 = upwin.TabItemControl(Name=names)
            elif i == 1:
                self.__group1 = upwin.PaneControl(Group=names)

    def getTab4(self):
        return self.__tab4

    def getGroup1(self):
        return self.__group1
