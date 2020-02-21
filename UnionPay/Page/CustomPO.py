#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"
class CustomPO():
    def __init__(self, locates):
        self.__locates = locates
        self.__tab2 = None
        self.__pane2 = None
        self.__tree2 = None

    def CustominitControl(self, upwin):
        for i in range(len(self.__locates)):
            tab2 = self.__locates[i][1]
            tabcontrol, names = tab2.split(":")
            if i == 0:
                self.__tab2 = upwin.TabItemControl(Name=names)
            elif i == 1:
                self.__pane2 = upwin.PaneControl(ClassName=names)
            elif i == 2:
                self.__tree2 = upwin.TreeItemControl(Name=names)

    def getTab2(self):
        return self.__tab2

    def getPane2(self):
        return self.__pane2

    def getTree2(self):
        return self.__tree2
