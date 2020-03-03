#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
import time

import uiautomation as auto
from Core import StepThree
from Page import CaseShowOnePO, CaseShowTwoPO, AuthPO, CustomPO


class StepTwo():
    def __init__(self, Logger, conf1, conf2, DataLoad):
        self._Conf1 = conf1
        self._Conf2 = conf2
        self._DataLoad = DataLoad
        self._CaseShowOnePO = None
        self._CaseShowTwoPO = None
        self._CustomPO = None
        self._AuthPo = None
        self._StepThree = None
        self._log = Logger
        self.stemTwoinitControl()

    def stemTwoinitControl(self):
        self.clickout = int(self._Conf1.get("timeout", "clickout"))
        self.logwait = int(self._Conf1.get("timeout", "logwait"))
        self.click_menu = int(self._Conf1.get("timeout", "click_menu"))
        self.intputtime = int(self._Conf1.get("timeout", "inputtime"))
        self._CaseShowOnePO = CaseShowOnePO.CaseShowOnePO(self._Conf2.items("CaseShowOne"))
        self._CaseShowOnePO.CaseShowOneinitControl(auto)
        self._CaseShowTwoPO = CaseShowTwoPO.CaseShowTwoPO(self._Conf2.items("CaseShowTwo"))
        self._CaseShowTwoPO.CaseShowTwoinitControl(auto)
        self._AuthPo = AuthPO.AuthPO(self._Conf2.items("AuthPO"))
        self._AuthPo.initControl(auto)
        self._CustomPO = CustomPO.CustomPO(self._Conf2.items("CostomPO"))
        self._CustomPO.CustominitControl(auto)
        self._StepThree = StepThree.StepThree(self._Conf1, self._Conf2, self._log)
        self._StepThree.StepThreeinitcontrol()

    def rootCardInfo(self):
        while 1:
            try:
                group = auto.GroupControl(Name='账号基本信息').GetChildren()
                combo = group[2]
                break
            except:
                tab = auto.TabControl(AutomationId='mainTab').TabItemControl(
                    Name='emd.ViewModel.ColGridViewModel')
                tab.DoubleClick()
                continue
        try:
            auto.PaneControl(AutomationId='scroll').GetScrollPattern().SetScrollPercent(
                horizontalPercent=-1, verticalPercent=100)
            self._log.info(f"滚动到选择卡号的位置")
        except:
            pass
        return combo

    def cards(self, combo, i, ii):
        while 1:
            try:
                self.stemTwoinitControl()
                data = self.getInputData(i, ii)
                card1 = data.get("卡号1")
                self._log.info(f"获得到的卡1数据是>>: {card1}")
                base_name = combo.GetSelectionPattern().GetSelection()[0].Name
                if len(re.compile(card1).findall(base_name)) != 0:
                    self._log.info(f'以选择案例卡号>: {base_name}')
                else:
                    combo.Click()
                card_id_list = [i for i in combo.GetChildren() if i.ClassName == 'ListBoxItem' and i.Name]
                for card_id in card_id_list:
                    if len(re.compile(card1).findall(card_id.Name)) != 0:
                        combo.Select(card_id.Name)
                break
            except Exception as e:
                tab = auto.TabControl(AutomationId='mainTab').TabItemControl(Name="emd.ViewModel.ColGridViewModel")
                tab.DoubleClick()
                auto.PaneControl(AutomationId='scroll').GetScrollPattern().SetScrollPercent(horizontalPercent=-1,
                                                                                            verticalPercent=100)
                self._log.error(f"卡号对象消失，正在重新查找，报错信息为{e}")
                continue

    def SaveButton(self):
        while 1:
            try:
                locating = auto.DataGridControl(
                    AutomationId='DataGrid1').HeaderControl().HeaderItemControl().TextControl()
                locating_x = locating.GetClickablePoint()[0]
                locating_y = locating.GetClickablePoint()[1] - 40
                auto.Click(locating_x, locating_y)
                self._log.info(f"点击保存按钮")
                break
            except Exception as e:
                tab = auto.TabControl(AutomationId='mainTab').TabItemControl(Name='emd.ViewModel.ColGridViewModel')
                tab.DoubleClick()
                self._log.error(f"输入对象丢失，正在重新查找，报错信息为{e}")
                continue

    def execase(self):
        execute_button = auto.CustomControl(ClassName='SideBarTabItemView_3').ImageControl()
        execute_button.Click()
        self._log.info("点击发送报文按钮")

    def inputPoName(self, pathName):
        time.sleep(self.clickout)
        case_lists = []
        case_list = auto.TreeItemControl(ClassName='TreeViewItem').GetChildren()
        for case in case_list:
            if case.ClassName == "TreeViewItem":
                case_lists.append(case)
        self._log.info(f"开始得到自定义案例集里所有的案例")
        for case in case_lists:
            if pathName == case.TextControl().Name:
                self._log.info(f"判断{pathName}<<<是否等于>>>: {case.TextControl().Name}")
                sure = case.GetScrollItemPattern().ScrollIntoView()
                if sure is True:
                    case.TextControl().Click()
                    case.TextControl().DoubleClick()
                    time.sleep(self.clickout)
                    self._log.info(f"点击>>>: {pathName}")
                else:
                    self._log.info(f"点击失败了，重新点击一下")
                    auto.PaneControl(ClassName='ScrollViewer').Click()
                    case.GetScrollItemPattern().Scrol1IntoView()
                    case.TextControl().Click()
                return case

    def addListTwo(self, case, select_item):
        custom_select_dict = {
            '银联发出的报文': 0,
            '银联接收的报文': 1,
            '删除案例': 2,
        }

        case.DoubleClick()
        self._log.info(f'点击：{case.Name}')
        case.RightClick()
        time.sleep(self.clickout)
        select_list = auto.MenuItemControl(ClassName='MenuItem').GetParentControl().GetChildren()
        number = custom_select_dict[select_item]
        selection = select_list[number].TextControl()
        self._log.info(f'选择菜单：{selection.Name}-选项')
        selection.Click()

    def getInputData(self, exeNo, selectNo):
        self._log.info("多条案例的执行数据处理")
        PO = self._DataLoad.load()
        POname = PO[4]
        cardName = POname.setExeCaed()
        newMap = {}
        for i in cardName[int(exeNo)].keys():
            if i.endswith("#" + str(selectNo)):
                b = i.split("#")
                newMap[b[0]] = cardName[int(exeNo)].get(i)
        self._log.info(f"处理后的案例数据为》》》{newMap}")
        return newMap

    def AsendData(self, No1, No2):
        data = self.getInputData(No1, No2)
        self._log.info("删除卡号1")
        data.pop("卡号1")
        try:
            data.pop("卡号2")
            self._log.info("删除卡号2")
        except:
            pass
        for field in data:
            self._log.info(f"输入的值为》》》{field},value>>>{data[field]}")
            self.input_text(field, data[field], 1)

    def input_text(self, field, message, num):
        while 1:
            try:
                search = auto.EditControl(AutomationId='SearchFrame')
                search.SendKeys('{Ctrl}a{Delete}')
                self._log.info('搜索字段：{}'.format(field))
                search.SendKeys(field + '{Enter}')
                try:
                    fieldInput = self._CaseShowTwoPO.getTab6()(Name=field).GetParentControl().GetChildren()[2]
                    fieldInput.DoubleClick()
                    time.sleep(self.clickout)
                    send = fieldInput.EditControl()
                    self._log.info('填写字段：{}-->{}'.format(field, message))
                    send.SendKeys('{Ctrl}a{Delete}')
                    send.SendKeys(message + '{Enter}')
                except LookupError:
                    self._log.error('案例序号：{}，字段:{},名称有误，请检查'.format(num, field))
                    return False, field
                break
            except Exception as e:
                tab = auto.TabControl(AutomationId='mainTab').TabItemControl(Name='emd.ViewModel.ColGridViewModel')
                tab.DoubleClick()
                self._log.error(f"输入对象丢失，正在重新查找，报错信息为{e}")
                continue

    def getCaseShowOnePO(self):
        return self._CaseShowOnePO

    def getCaseShowTwoPO(self):
        return self._CaseShowTwoPO

    def getCustomPO(self):
        return self._CustomPO
