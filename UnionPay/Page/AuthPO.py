#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"


class AuthPO():
    def __init__(self, locate):
        self.__locate = locate
        self.__tab1 = None
        self.__pane1 = None
        self.__list1 = None
        self.__tree1 = None
        self.__button = None

    def initControl(self, upwin):
        for i in range(len(self.__locate)):
            tab1 = self.__locate[i][1]
            tabcontrol, name = tab1.split(":")
            if i == 0:
                self.__tab1 = upwin.TabItemControl(Name=name)
            elif i == 1:
                self.__pane1 = upwin.PaneControl(ClassName=name)
            elif i == 2:
                self.__tree1 = upwin.TreeItemControl(Name=name)
            elif i == 3:
                self.__list1 = upwin.ListControl(ClassName=name)
        self.__button = upwin.ButtonControl

    def getTab1(self):
        return self.__tab1

    def getPane1(self):
        return self.__pane1

    def getTree1(self):
        return self.__tree1

    def getList1(self):
        return self.__list1

    def getButton1(self):
        return self.__button
