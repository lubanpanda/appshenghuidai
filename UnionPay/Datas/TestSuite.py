#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

class TestSuite():
    def __init__(self, testCases):
        self.__testCases = testCases
        self.__exeList = []
        self.__exeListNum = 0
        self.__exePathNo = []

    def setExeList(self):
        "执行案例的次数和添加案例的行号"
        for i in range(len(self.__testCases)):
            if self.__testCases[i].getFlag() is True:
                self.__exeList.append(i)
                self.__exePathNo.append(self.__testCases[i].getPathNum())
        self.__exeListNum = len(self.__exeList)
        return self.__exeListNum, self.__exeList, self.__exePathNo

    def setExeCaed(self):
        info = []
        for i in range(len(self.__testCases)):
            if self.__testCases[i].getFlag() is True:
                info.append(self.__testCases[i].getDataMap())
        return info

    def getTestCases(self):
        return self.__testCases

    def getExelist(self):
        return self.__exeList

    def getExeListNum(self):
        return self.__exeListNum

    def __str__(self):
        pass
