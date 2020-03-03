#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class CasePath():
    def __init__(self, pathNo, pathList):
        self.__pathNo = pathNo
        self.__pathList = pathList

    def getPathNo(self):
        return self.__pathNo

    def getPathList(self):
        return self.__pathList
