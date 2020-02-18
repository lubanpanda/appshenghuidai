#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"


class CasePaths():
    def __init__(self, casePaths):
        self.__casePaths = casePaths
        self.__exePath = []
        self.__pathNum = len(casePaths)

    def setPathList(self, exePathNo):
        for i in exePathNo:
            for a in range(len(self.__casePaths)):
                if self.__casePaths[a].getPathList == i:
                    self.__exePath.append(self.__casePaths[a].getPathList())
        self.__pathNum = len(self.__casePaths)
        return self.__exePath

    def getCasePaths(self):
        return self.__casePaths

    def getPathNum(self):
        return self.__pathNum
