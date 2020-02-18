import configparser
import datetime
import os
import re
import time

import uiautomation as auto

from UnionPay import common


class CustomCaseSet:
    def __init__(self, logger):
        self.case_list = []
        self.cus = common.Common(logger)
        conf = configparser.ConfigParser()
        conf.read(os.getcwd() + r'\settings\config.ini', encoding='utf-8')
        self.AXIS_Y = int(conf.get('normal_config', 'save_button_axis_Y'))
        self.logger = logger  # 日志对象初始化
        self.get_case_list()  # 初始化时自动获取自定义案例集的案例列表

    # 点击切换至自定义案例集
    def click_self(self):
        a = auto.TabItemControl(Name='自定义案例集')
        a.DoubleClick()
        button = auto.ButtonControl(AutomationId='Expander')
        self.cus.unfold(button)

    # 获取自定义案例集左菜单栏的案例列表
    def get_case_list(self):
        self.logger.info('正在获取自定义案例集案例列表...')
        self.case_list = []
        case_list = auto.TreeItemControl(ClassName='TreeViewItem').GetChildren()
        for case in case_list:
            if case.ClassName == 'TreeViewItem':
                self.case_list.append(case)
                self.logger.info('自定义案例：{}'.format(case.TextControl().Name))
        self.logger.info('获取自定义案例集案例列表成功')
        return len(self.case_list)

    # 选择卡号
    def select_card_id(self, comboitem: str, card_number: str, num):
        group = auto.GroupControl(Name='账号基本信息').GetChildren()
        combo = group[2]

        # 判断是否存在-卡号2
        if card_number == '卡号2':
            combo = group[4]
        base_name = combo.GetSelectionPattern().GetSelection()[0].Name

        # 如果选项框中是已选卡号则不做选择
        if len(re.compile(comboitem).findall(base_name)) != 0:
            self.logger.info('已选择卡号：{}'.format(base_name))
            return
        combo.Click()
        pane = auto.ListItemControl(Name=base_name).GetParentControl()
        button_group = pane.ScrollBarControl(AutomationId='VerticalScrollBar').GetChildren()

        button_up = button_group[1]  # 选择卡号框点击可以使滚动条向上的按钮
        button_down = button_group[3]  # 选择卡号框点击可以使滚动条向下的按钮
        button_click_down = button_group[4]  # 选择卡号矿点击可以使滚动条向下滚动一条卡号信息的按钮
        while True:  # 将滚动条置顶
            if str(button_up.BoundingRectangle) != '(0,0,0,0)[0x0]':
                button_up.Click()
                time.sleep(self.cus.click_time)
            else:
                break

        # 获取选择卡号框中所有的卡号信息的名字
        card_id_list = [i for i in combo.GetChildren() if i.ClassName == 'ListBoxItem' and i.Name]
        flag = False
        for card_id in card_id_list:
            if len(re.compile(comboitem).findall(card_id.Name)) != 0:
                card = auto.ListItemControl(Name=card_id.Name)
                self.cus.clickloop(button_down, card, button_click_down)
                card.Click()
                time.sleep(self.cus.click_time)

                base_name = combo.GetSelectionPattern().GetSelection()[0].Name
                if len(re.compile(comboitem).findall(base_name)) == 0:
                    self.select_card_id(comboitem, card_number, num)

                self.logger.info('已选择卡号：{}'.format(card_id.Name))
                flag = True
                break
        if flag is False:
            self.logger.error('案例序号：{}，不存在卡号-->{}，请填写正确卡号'.format(num, comboitem))
            print('案例序号：{}，不存在卡号-->{}，请填写正确卡号'.format(num, comboitem))
            combo.Click()
            return False
        elif flag is True:
            return True

    def edit_field(self, field, message, num):
        search = auto.EditControl(AutomationId='SearchFrame')
        search.SendKeys('{Ctrl}a{Delete}')
        self.logger.info('搜索字段：{}'.format(field))
        search.SendKeys(field + '{Enter}')
        # 报文信息填写域
        try:
            fieldInput = auto.CustomControl(Name=field).GetParentControl().GetChildren()[2]
            fieldInput.DoubleClick()
            time.sleep(self.cus.click_time)
            send = fieldInput.EditControl()
            self.logger.info('填写字段：{}-->{}'.format(field, message))
            send.SendKeys('{Ctrl}a{Delete}')
            send.SendKeys(message + '{Enter}')
            time.sleep(self.cus.click_time)
        except LookupError:
            self.logger.error('案例序号：{}，字段:{},名称有误，请检查'.format(num, field))
            print('案例序号：{}，字段:{},名称有误，请检查'.format(num, field))
            return (False, field)

    def empty_case_list(self):
        self.logger.info('正在清空自定义案例集...')
        auto.TabItemControl(Name='自定义案例集').DoubleClick()
        self.get_case_list()
        lens = len(self.case_list)
        while lens > 0:
            self.logger.info('删除案例：{}'.format(self.case_list[0].TextControl().Name))
            self.cus.select_menu(case=self.case_list[0].TextControl(), select_item='删除案例', custom_='custom')
            self.get_case_list()
            time.sleep(self.cus.click_time)
            lens = len(self.case_list)
        self.logger.info('清空自定义案例集完成')

    def save(self):
        locating = auto.DataGridControl(AutomationId='DataGrid1').HeaderControl().HeaderItemControl().TextControl()
        locating_x = locating.GetClickablePoint()[0]
        locating_y = locating.GetClickablePoint()[1] - self.AXIS_Y
        self.logger.info('点击保存按钮')
        auto.Click(locating_x, locating_y)
        time.sleep(self.cus.click_time)
        self.logger.info('保存案例修改')

    def execute_case(self):
        execute_button = auto.CustomControl(ClassName='SideBarTabItemView_3').ImageControl()
        self.logger.info('点击执行按钮')
        execute_button.Click()
        time.sleep(self.cus.click_time)
        self.logger.info('执行案例')
        self.logger.info('等待返回报文，时间为10s')
        time.sleep(self.cus.get_log_time)

    def log_information(self, id, number: str, case_type: str, result, summary_file):
        """

        :param id: 案例序号
        :param number: 案例编号
        :param case_type: 案例类型
        :param result: 技术描述f39
        :param summary_file: 汇总的docx文件（word）
        :return:
        """
        self.logger.info('正在获取日志信息...')
        tab = auto.TabControl(AutomationId='mainTab').TabItemControl(Name='emd.ViewModel.CustomLogViewModel')
        self.logger.info('点击日志信息')
        tab.DoubleClick()
        time.sleep(self.cus.click_time)
        document = auto.DocumentControl(ClassName='FlowDocumentScrollViewer').DocumentControl(AutomationId='flow')
        self.logger.info('点击日志文本区')
        time.sleep(self.cus.click_time)

        # 检查日志报文中是否有相对应的返回码
        split_pat = 'MessageBegin(.*?)MessageEnd'
        log_f39 = ''  # 日志中的F39值
        expected_f39 = result  # 期望的F39值
        excute_list = []  # 存放是否查找到返回码字段的结果最后一个是F39返回码
        complete_content = document.GetTextPattern().DocumentRange.GetText()  # 日志主体
        clean_content = complete_content.replace('\n', '').replace('\r', '').replace(' ', '')
        split_content = re.compile(split_pat).findall(clean_content)
        content = split_content[-1] if len(split_content) != 0 else ''  # 截取最后一段完整报文
        result_field = [i.replace(' ', '') for i in self.cus.result_list]  # 需要获取的返回码字段
        for field in result_field:
            new = r'\[' + str(field) + r'\]:\[(.*?)\]'
            result = re.compile(new).findall(content)
            self.logger.info('正在匹配返回报文中的返回码：{}'.format(field))
            excute_list.append(result[-1] if len(result) != 0 else '')
            self.logger.info('匹配成功，{}为{}'.format(field, result[-1]) if len(result) != 0 else '匹配{}失败'.format(field))
            if field == 'F39应答码':
                log_f39 = result[-1] if len(result) != 0 else ''

        # 判断——报文检查失败——是否存在于日志中
        is_fail = True if '报文检查失败' in complete_content else False
        check = '' if is_fail is False else re.compile(r'(报文检查.*)', re.S).findall(complete_content)[0]

        # 获得执行结果
        if expected_f39 is None:
            excute_list.append('00')
            final = False if log_f39 != '00' else True
            excute_list.append(check)
        else:
            excute_list.append(','.join(expected_f39))
            final = False if log_f39 not in expected_f39 else True
            excute_list.append(check)
        excute_list.append(final)

        name_pat = '系统运行状态信息：(.*?)开始发送报文'
        co_name = number + re.compile(name_pat).findall(clean_content)[0]
        file_name = co_name.replace('/', '-') + '.txt'
        for ch in [i for i in range(0, 38)]:
            if chr(ch) != '\n':
                complete_content = complete_content.replace(chr(ch), ' ')
        summary_file.add_heading('{}'.format(co_name))
        summary_file.add_paragraph('{}'.format(complete_content))

        clean_button = auto.ButtonControl(ClassName='Button', Name='清空')
        # 如果是单案例或者是多案例的最后一个案例，则执行清空日志操作
        if case_type == 'case' or case_type == 'caseEnd':
            clean_button.DoubleClick()
            self.logger.info('清空界面日志信息')

            today = datetime.datetime.now().strftime('%Y-%m-%d')
            path = os.getcwd() + r'\log_files\case_log_files\{}'.format(today)
            if not os.path.exists(path):
                os.makedirs(path)
            file_name = path + r'\{}'.format(file_name)

            # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            with open(file_name, 'a', encoding='utf-8') as f:
                self.logger.info('写入日志信息')
                f.write(complete_content)

            self.logger.info('日志信息获取完毕')
        return [str(id)] + excute_list
