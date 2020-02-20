#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import os

import xlrd

from UnionPay.Datas import TestCase, TestSuite, CasePath, CasePaths
from UnionPay.Logs.logs import Logs


class DataLoad():
    def __init__(self, casePath, templatePath):
        self.__casePath = casePath
        self.__templatePath = templatePath
        self.__log = Logs().Loginit()

    def load(self):
        paths = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        try:
            file = xlrd.open_workbook(paths + r'\Files\{}'.format(self.__casePath))
        except FileNotFoundError as e:
            self.__log.error("该文件名不存在，请检查文件配置", e)
            exit()
        table = file.sheet_by_index(0)
        suite = []
        fields = table.row_values(0)
        for i in range(table.nrows - 1):
            rowfield = table.row_values(i + 1)
            caseNo = str(rowfield[0])
            flag = False
            if rowfield[1] == "Y":
                flag = True
            pathNo = rowfield[2]
            apathno = pathNo.split(",")
            dataMap = {}
            for a in range(3, len(rowfield)):
                if rowfield[a] == None:
                    dataMap[fields[a]] = ""

                else:
                    dataMap[fields[a]] = rowfield[a]
                testcase = TestCase.TestCase(caseNo, flag, apathno, dataMap)
                suite.append(testcase)
            testSuite = TestSuite.TestSuite(suite)
            pathss = testSuite.setExeCaed()
            pathss1 = pathss[1]
            paths = pathss[2]
            exelistNo = []
            for i in range(len(paths)):
                for a in paths[i]:
                    exelistNo.append(a)
            try:
                pathss = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                pathfFile = xlrd.open_workbook(pathss + r'\Files\{}'.format(self.__templatePath))
            except FileNotFoundError as e:
                self.__log.error("路径文件不存在，请检查配置文件", e)
            pathHead = pathfFile.sheet_by_index(0)
            pathList = []
            for i in range(pathHead.nrows - 1):
                rowfield = pathHead.row_values(i + 1)
                pathNo = rowfield[0]
                pathsuite = []
                for a in range(1, len(rowfield)):
                    pathsuite.append(rowfield[a])
                testcase = CasePath.CasePath(pathNo, pathsuite)
                pathList.append(testcase)
            casePaths = CasePaths.CasePaths(pathList)
            casePathName = casePaths.setPathList(exelistNo)
            casePathss = CasePaths.CasePaths(pathList)
            casePathNamess = casePathss.setPathList(list(set(exelistNo)))
            return pathss1, casePathNamess, casePathName, paths, testSuite
