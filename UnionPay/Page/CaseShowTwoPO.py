#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class CaseShowTwoPO():
    def __init__(self, locate):
        self.__locate = locate
        self.__tab5 = None
        self.__tab6 = None

    def CaseShowTwoinitControl(self, upwin):
        for i in range(len(self.__locate)):
            tab2 = self.__locate[i][1]
            tabcontrol, names = tab2.split(":")
            if i == 0:
                self.__tab5 = upwin.EditControl(AutomationId=names)
        self.__tab6 = upwin.CustomControl

    def getTab5(self):
        return self.__tab5

    def getTab6(self):
        return self.__tab6
