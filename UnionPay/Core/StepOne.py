#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

import uiautomation as auto

from UnionPay.Page import AuthPO, CustomPO


class StepOne():
    def __init__(self, Logger, conf1, conf2, DataLoad):
        self.__Conf1 = conf1
        self.__Conf2 = conf2
        self.__DataLoad = DataLoad
        self.__upwin = None
        self.__AuthPO = None
        self.__CustomPO = None
        self.__log = Logger
        self.setpOneinitControl()

    def setpOneinitControl(self):
        self.clcikout = int(self.__Conf1.get("timeout", "clickout"))
        self.logwait = int(self.__Conf1.get("timeout", "logwait"))
        self.click_menu = int(self.__Conf1.get("timeout", "click_menu"))
        self.inputtime = int(self.__Conf1.get("timeout", "inputtime"))
        self.__AuthPO = AuthPO.AuthPO(self.__Conf2.items("AuthPO"))
        self.__AuthPO.initControl(auto)
        self.__CustomPO = CustomPO.CustomPO(self.__Conf2.items("CostomPO"))
        self.__CustomPO.CustominitControl(auto)

    "左侧栏向右最大化"
    def rigthSide(self):
        try:
            splitter = auto.ThumbControl(ClassName='GridSplitter').GetClickablePoint()
            if splitter[0] < 400:
                auto.DragDrop(splitter[0], splitter[1], 600, splitter[1], 1)
                self.__log.info("左侧栏滑倒最右端")
        except:
            pass

    "添加案例"
    def addCase(self):
        self.__log.info("正在开始添加案例......")
        casepath = self.__DataLoad.load()[1]
        self.__log.info(f"获取到了案例数据>>>:{casepath}")
        self.__AuthPO.getTab1().DoubleClick()
        count = 0
        for case in casepath:
            if count > 0:
                if case[0] != casepath[count - 1][0]:
                    # 寻找左下角路径
                    self.clickLeftMeus(case[0])
            else:
                self.clickLeftMeus(case[0])
            self.findCase(case)
            count += 1

    def CaseCompartion(self):
        self.__log.info("开始进行案例对比")
        self.__CustomPO.getTab2().DoubleClick()
        oldcase = []
        newCase = {}
        exeNewList = []
        for i in range(len(self.getCaseList())):
            oldcase.append(self.getCaseList()[i].TextControl().Name)
        path = self.__DataLoad.load()
        for i in range(len(path[1])):
            newCase[path[1][i][-1]] = path[1][i]
        for i in range(len(newCase)):
            if path[1][i][-1] in oldcase:
                newCase.pop(path[1][i][-1])
        for a in newCase.values():
            exeNewList.append(a)
        self.__log.info(f"添加案例失败的路径是{exeNewList}")
        if len(exeNewList) == 0:
            self.__log.info(f"没有需要额外添加的案例")
        else:
            self.__AuthPO.getTab1.DoubleClick()
            self.__log.info(f"开始执行失败案例的添加")
            count = 0
            for case in exeNewList:
                if count > 0:
                    if case[0] != exeNewList[count - 1][0]:
                        self.clickLeftMeus(case[0])
                else:
                    self.clickLeftMeus(case[0])
                self.findCase(case)
                count += 1

    def findCase(self, case_list):
        self.__log.info("开始查找案例")
        count = 0
        flag = True
        root = self.__AuthPO.getTree1().TextControl(Name=case_list[0])
        temp_list = [i for i in root.GetParentControl().GetChildren() if i.Name == 'emd.ViewModel.SubLevelViewModel']
        for path in range(1, len(case_list)):  # 从路径的第二个开始搜索
            for i in temp_list:
                focus_path = case_list[path]
                if i.TextControl().Name == case_list[path]:
                    count += 1
                    if i.ButtonControl():
                        try:
                            if i.ButtonControl().GetTogglePattern().ToggleState == 0:
                                i.GetExpandCollapsePattern().Expand(0)
                        except:
                            pass
                        # 获取展开节点的子节点
                        temp_list = [temp for temp in i.GetChildren() if temp.Name == 'emd.ViewModel.SubLevelViewModel']
                        if path == len(case_list) - 1:
                            self.__log.info(f"自动滚到{case_list[path]}路径下")
                            i.GetScrollItemPattern().ScrollIntoView()
                            i.TextControl().Click()
                            self.addList(i.TextControl(), "案例另存为自定义案例集")

        if count < len(case_list) - 1:
            self.__log.error(f'案例路径:{focus_path}书写错误，未找到该路径，请检查路径文件！')
            print(f'案例路径:{focus_path}书写错误，未找到该路径，请检查路径文件！')
            input("请按任意键退出。。。")
            exit(0)
        if flag is False:
            self.__log.error(f'案例路径:{focus_path}书写错误，未找到该路径，请检查路径文件！')
            print(f'案例路径:{focus_path}书写错误，未找到该路径，请检查路径文件！')
            input("请按任意键退出。。。")
            exit(0)

    def addList(self, case, select_item):
        certification_select_dict = {
            '案例另存为自定义案例集': 0,
            '银联发出的报文': 1,
            '银联接收的报文': 2,
        }
        case.DoubleClick()
        time.sleep(self.clcikout)
        case.RightClick()
        select_list = auto.MenuItemControl(ClassName='MenuItem').GetParentControl().GetChildren()
        number = certification_select_dict[select_item]
        selection = select_list[number].TextControl()
        self.__log.info('选择菜单：{}-选项'.format(selection.Name))
        selection.Click()

    def clickLeftMeus(self, meusname):
        self.__log.info("选择左侧菜单栏")
        self.__AuthPO.getList1().GetScrollPattern().SetScrollPercent(-1, 0)
        flag = False
        for i in self.__AuthPO.getList1().GetChildren():
            if i.Name == meusname:
                flag = True
                i.GetScrollItemPattern().ScrollIntoView()
                i.Click()
                self.__log.info(f"自动滚到》》》{meusname}，并去点击它")

        if flag is False:
            self.__log.error(f'没有路径--{meusname}，请检查路径')
            print(f'没有路径--{meusname}，请检查路径')
            input("请按任意键退出。。。")
            exit(0)

    def clearCase(self):
        self.__log.info("开始执行清空自定义案例集")
        self.__CustomPO.getTab2().DoubleClick()
        self.getCaseList()
        lens = len(self.getCaseList())
        while lens > 0:
            try:
                self.deleteList(self.getCaseList()[0].TextControl(), select_item="删除案例")
                self.__log.info("删除案例成功")
            except:
                self.__log.info("自定义案例集里的所有案例删除成功")
                break

    def deleteList(self, case, select_item):
        custom_select_dict = {
            '银联发出的报文': 0,
            '银联接收的报文': 1,
            '删除案例': 2,
        }
        case.DoubleClick()
        self.__log.info('点击：{}'.format(case.Name))
        case.RightClick()
        time.sleep(self.clcikout)
        select_list = auto.MenuItemControl(ClassName='MenuItem').GetParentControl().GetChildren()
        number = custom_select_dict[select_item]
        selection = select_list[number].TextControl()
        self.__log.info('选择菜单：{}-选项'.format(selection.Name))
        selection.Click()

    def click_self(self):
        self.__log.info("点击【认证案例集】")
        return self.__AuthPO.getTab1().DoubleClick()

    def getCaseList(self):
        case_lists = []
        case_list = auto.TreeItemControl(ClassName='TreeViewItem').GetChildren()
        for case in case_list:
            if case.ClassName == 'TreeViewItem':
                case_lists.append(case)
        return case_lists

    def getDataLoad(self):
        return self.__DataLoad

    def getstepOneUpwin(self):
        return self.__upwin

    def getAuthPo(self):
        return self.__AuthPO

    def getCustomPo(self):
        return self.__CustomPO
