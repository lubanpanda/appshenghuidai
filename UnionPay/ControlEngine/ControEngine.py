#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import docx
import uiautomation as auto

from UnionPay.Biz import DataLoad
from UnionPay.Config import Conf
from UnionPay.Core import StepOne, StepTwo, StepThree
from UnionPay.Logs.logs import Logs
from UnionPay.SaveFile import SaveWord, SaveExcel


class ControlEngine():
    def __init__(self):
        # 三个页面对象
        self._DataLoad = None
        self._StepOne = None
        self._StepTwo = None
        self._StepThree = None
        self._Log = None

    def ControlEngineinitControl(self):
        self._Log = Logs()
        self._Log.Loginit()
        Logger = self._Log.getLogger()
        conf = Conf.Conf().readConf(os.getcwd() + r"\Config\configone.ini")
        conf2 = Conf.Conf().readConf(os.getcwd() + r"\Config\configtwo.ini")
        casePath = conf.get("paths", "casePath")
        templatePath = conf.get("paths", "templatePath")
        self._DataLoad = DataLoad.DataLoad(casePath, templatePath)
        self._StepOne = StepOne.StepOne(Logger, conf, conf2, self._DataLoad)
        self._StepTwo = StepTwo.StepTwo(Logger, conf, conf2, self._DataLoad)
        self._StepThree = StepThree.StepThree(conf, conf2, Logger)
        auto.SetGlobalSearchTimeout(10)

    def run(self, rootInput):
        self.ControlEngineinitControl()
        if rootInput == "1":
            auto.WindowControl(Name='中国银联入网测试仿真系统（机构版）').SwitchToThisWindow()
            auto.WindowControl(Name='中国银联入网测试仿真系统（机构版）').Maximize()
            self._StepOne.rigthSide()
            self._StepOne.clearCase()
            self._StepOne.click_self()
            self._StepOne.addCase()
        elif rootInput == "2":
            auto.WindowControl(Name='中国银联入网测试仿真系统（机构版）').SwitchToThisWindow()
            auto.WindowControl(Name='中国银联入网测试仿真系统（机构版）').Maximize()
            self._StepOne.rigthSide()
        self._StepOne.CaseCompartion()
        self._StepThree.clean_log()
        Nus = self._DataLoad.load()
        wordPO = docx.Document()
        caseNo = Nus[0]
        b = Conf.Conf().readConf(os.getcwd() + r"\Config\configone.ini")
        casepath = b.get('paths', 'casePath')
        PO = self._DataLoad.load()
        pathss = PO[3]
        POName = PO[2]
        getResultlist = []
        wordsList = []
        getAllCase = None
        b = 0
        Noss = []
        for s in range(len(PO[0])):
            Nos = caseNo[s] + 1
            Noss.append(Nos)
            if len(pathss[s]) == 1:
                name = POName[b][-1]
                self._StepTwo.inputPoName(name)
                combo = self._StepTwo.rootCardInfo()
                self._StepTwo.cards(combo, s, 1)
                self._StepTwo.addListTwo(self._StepTwo.inputPoName(name).TextControl(), '银联发出的报文')
                self._StepTwo.AsendData(s, 1)
                self._StepTwo.SaveButton()
                self._StepTwo.execase()
                self._StepThree.boncedShow()
                a = self._StepThree.getSaveInfo(wordPO, Nos)
                getResultlist.append(a[0])
                getAllCase = a[1]
                self._StepThree.clean_log()
                b += 1
            else:
                for i in range(len(pathss[s])):
                    name = POName[b][-1]
                    self._StepTwo.inputPoName(name)
                    combo = self._StepTwo.rootCardInfo()
                    self._StepTwo.cards(combo, s, i + 1)
                    self._StepTwo.addListTwo(self._StepTwo.inputPoName(name).TextControl(), '银联发出的报文')
                    self._StepTwo.AsendData(s, i + 1)
                    self._StepTwo.SaveButton()
                    self._StepTwo.execase()
                    self._StepThree.boncedShow()
                    a = self._StepThree.getSaveInfo(wordPO, Nos)
                    getResultlist.append(a[0])
                    getAllCase = a[1]
                    wordsList.append(a[2])
                    b += 1
                self._StepThree.clean_log()
        SaveWord.SaveWord(wordPO, casepath)
        SaveExcel.SaveExcel(casepath, getAllCase, getResultlist)
        return getResultlist
