#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import uiautomation as auto

from UnionPay.Biz import DataLoad
from UnionPay.Config import Conf
from UnionPay.Core import StepOne, StepTwo, StepThree
from UnionPay.Logs.logs import Logs


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
        conf = Conf.Conf().readConf(" config1. ini")
        casePath = conf.get('paths', ' casePath')
        templatePath = conf.get('paths', ' templatePath')
        conf2 = Conf.Conf().readConf("config2. ini")
        self._DataLoad = DataLoad.DataLoad(casePath, templatePath)
        self._StepOne = StepOne.StepOne(Logger, conf, conf2, self._DataLoad)
        self._StepTwo = StepTwo.StepTwo(conf, conf2, self._DataLoad, Logger)
        self._StepThree = StepThree.StepThree(conf, conf2, Logger)
        auto.SetGlobalSearchTimeout(10)

    def run(self, rootInput):
        self.ControlEngineinitControl()
        if rootInput == "1":
            auto.WindowControl(Name="中国银联入网测试仿真系统（机构版）").SwitchToThisWindow()
            auto.WindowControl(Name="中国银联入网测试仿真系统（机构版）").Maximize()
            self._StepOne.rigthSide()
            self._StepOne.clearCase()
            self._StepOne.click_self()
            self._StepOne.addCase()
        elif rootInput == "2":
            auto.WindowControl(Name="中国银联入网测试仿真系统（机构版）").SwitchToThisWindow()
            auto.WindowControl(Name="中国银联入网测试仿真系统（机构版）").Maximize()
            self._StepThree.clean_log()
            self._StepOne.rigthSide()
        self._StepOne.CaseCompartion()
        result = self._StepTwo.selectCard()
        return result


if __name__ == '__main__':
    a = ControlEngine()
    a.run(1)
