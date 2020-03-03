#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class TestCase():
    def __init__(self, caseNo, flag, pathNo, dataMap):
        self.__caseNo = caseNo
        self.__flag = flag
        self.__pathNo = pathNo
        self.__dataMap = dataMap

    def getCaseNo(self):
        return self.__caseNo

    def __str__(self):
        pass

    def getPathNum(self):
        return self.__pathNo

    def getDataMap(self):
        return self.__dataMap

    def getFlag(self):
        return self.__flag
