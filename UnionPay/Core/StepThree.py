#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import re

import uiautomation as auto

from UnionPay.Page import LogPO
from UnionPay.SaveFile import SaveCaseLog


class StepThree():
    def __init__(self, conf1, conf2, Logger):
        self._upwin = None
        self._log = Logger
        self._Conf1 = conf1
        self._Conf2 = conf2
        self._Allcase = []  # 5T1
        self._result_list = []
        self.StepThreeinitcontrol()

    def StepThreeinitcontrol(self):
        self._LogPO = LogPO.LogPO(self._Conf2.items("LogPO"))
        self._LogPO.LogPOinitControl(auto)
        self.clickout = int(self._Conf1.get("timeout", "clickout"))
        self.logwait = int(self._Conf1.get("timeout", "logwait"))
        self.click_menu = int(self._Conf1.get("timeout", "click_ menu"))
        self.intputtime = int(self._Conf1.get("timeout", " intputtime"))

    def getLogInfomation(self):
        self.StepThreeinitcontrol()
        tab = self._LogPO.getTab6().TabItemControl(Name="emd.ViewModel.CustomLogViewModel")
        tab.DoubleClick()
        # time.sleep(self.clickout)
        document = self._LogPO.getcont().DocumentControl(AutomationId=" flow")
        text = document.GetTextPattern().DocumentRange.GetText()
        # time.sleep(self.logwait)
        self._log.info(f"得到的报文文本信息是{text}")
        return text

    def boncedShow(self):
        while auto.WindowControl(Name="提示").Exists(1):
            auto.WindowControl(Name="提示").SetTopmost()
            try:
                auto.ButtonControl(Name="确定").Click()
                self._log.info("点击了报文弹窗确定按钮")
            except:
                pass

    def getSaveInfo(self, docu, caseNo):
        summary_file = docu
        split_pat = 'MessageBegin(.*?)MessageEnd'
        log_f39 = ''  # 日志中的F39值
        # expected_f39 = result  # 期望的F39值
        excute_list = []  # 存放是否查找到返回码字段的结果最后一个是F39返回码
        excute_list.append(caseNo)
        complete_content = self.getLogInfomation()

        clean_content = complete_content.replace('\n', '').replace('\r', '').replace(' ', '')
        split_content = re.compile(split_pat).findall(clean_content)

        content = split_content[-1] if len(split_content) != 0 else ''  # 截取最后一段完整报文
        self._result_list = [self._Conf1.get('save_field', '{}'.format(i)) for i in self._Conf1.options('save_field')]
        result_field = [i.replace(' ', '') for i in self._result_list]  # 需要获取的返回码字段
        for field in result_field:
            new = r'\[' + str(field) + r'\]:\[(.*?)\]'
            result = re.compile(new).findall(content)
            # self._log.info('正在匹配返回报文中的返回码：{}'.format(field))
            excute_list.append(result[-1] if len(result) != 0 else '')
            self._log.info('匹配成功，{}为{}'.format(field, result[-1]) if len(result) != 0 else '匹配{}失败'.format(field))
            if field == 'F39应答码':
                log_f39 = result[-1] if len(result) != 0 else ''
        self._log.info(f"获取匹配字段的值{excute_list}")
        excute_list.append(log_f39)
        # 判断——报文检查失败——是否存在于日志中
        is_fail = True if '报文检查失败' in complete_content else False
        check = '' if is_fail is False else re.compile(r'(报文检查.*)', re.S).findall(complete_content)[0]
        excute_list.append(check)
        self._log.info(f"匹配报文检查的信息>>>{check}")
        # 获得执行结果
        # if expected_f39 is None:
        #     excute_list.append('00')
        #     final = False if log_f39 != '00' else True
        #     excute_list.append(check)
        # else:
        #     excute_list.append(','.join(expected_f39))
        #     final = False if log_f39 not in expected_f39 else True
        #     excute_list.append(check)
        excute_list.append(check)

        # excute_list.append(','.join(expected_f39))
        final = False if log_f39 not in "00" else True
        excute_list.append(final)
        name_pat = '系统运行状态信息：(.*?)开始发送报文'
        co_name = re.compile(name_pat).findall(clean_content)[0]
        # file_name = co_name.replace('/', '-') + '.txt'
        for ch in [i for i in range(0, 38)]:
            if chr(ch) != '\n':
                complete_content = complete_content.replace(chr(ch), ' ')
        # summary_file.add_heading('{}'.format(co_name))
        # summary_file.add_paragraph('{}'.format(complete_content))
        summary_file.add_heading(str(caseNo) + "-" + f"{co_name}")
        summary_file.add_paragraph(f"{complete_content}")
        self._Allcase.append(excute_list)
        SaveCaseLog.SaveCaseLog(co_name, complete_content)
        return excute_list, result_field, summary_file

    def clean_log(self):
        self._log.info("清理执行发送报文时产生的日志")
        try:
            tab = auto.TabControl(AutomationId='mainTab').TabItemControl(Name="emd.ViewModel.CustomLogViewModel")
            tab.DoubleClick()
            clean_button = auto.ButtonControl(ClassName='Button', Name="清空")
            clean_button.DoubleClick()
        except LookupError:
            pass

    def getUpwin(self):
        return self._upwin

    def getAllcase(self):
        return self._Allcase

    def getResultList(self):
        return self._result_list

    def getLogPO(self):
        return self._LogPO
