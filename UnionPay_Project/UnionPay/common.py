import configparser
import datetime
import os
import re
import time

import docx
import uiautomation as auto
import xlrd
import xlwt

from UnionPay import certification_case_set


class Common:
    def __init__(self, logger):
        """
        初始化，拓宽左边侧栏
        :param logger: 日志对象
        """
        self.logger = logger
        conf = configparser.ConfigParser()
        conf.read(os.getcwd() + r'\settings\config.ini', encoding='utf-8')
        self.data_file = str(conf.get('data_file_path', 'field_data_file'))
        self.path_file = str(conf.get('data_file_path', 'path_data_file'))
        self.click_time = float(conf.get('time_config', 'click_time'))
        self.ordinary_time = float(conf.get('time_config', 'ordinary_time'))
        self.get_log_time = float(conf.get('time_config', 'get_log_time'))
        self.global_time = float(conf.get('time_config', 'set_global_timeout'))
        auto.SetGlobalSearchTimeout(self.global_time)
        self.result_list = [conf.get('field_data_file', '{}'.format(i)) for i in conf.options('field_data_file')]
        self.result_list.append('F39应答码')
        self.expected_F39 = []  # 技术描述的F39域
        self.execute_result = []  # 执行结果
        self.success_case = []  # 成功案例
        self.undo = []  # 未执行案例
        self.fail_case = []  # 失败案例
        self.whole_case = 0  # 总案例数
        self.summary_file = docx.Document()
        self.log = ''
        self.failure_reason = []

        try:
            splitter = auto.ThumbControl(ClassName='GridSplitter').GetClickablePoint()
            if splitter[0] < 400:
                time.sleep(self.ordinary_time)
                auto.DragDrop(splitter[0], splitter[1], 600, splitter[1], 1)
                time.sleep(self.click_time)
                self.logger.info('拓宽左侧栏')
        except:
            pass

    def unfold(self, element: auto.uiautomation.ButtonControl, **kwargs):
        """
        展开节点操作
        :param element:
        :return:
        """

        if element.GetTogglePattern().ToggleState == 0:
            # 如果该按钮不可见，则滑动至最左端
            if element.GetClickablePoint()[2] is False:
                try:
                    vertical = auto.PaneControl(
                        ClassName='ScrollViewer').GetScrollPattern().VerticalScrollPercent
                    auto.PaneControl(ClassName='ScrollViewer').GetScrollPattern().SetScrollPercent(
                        horizontalPercent=0, verticalPercent=vertical)
                except:
                    pass
            if kwargs:
                self.logger.info('展开：{}--选项'.format(kwargs['name']))
                element.Click()
                time.sleep(self.click_time)
                self.unfold(element)
            else:
                element.Click()
                time.sleep(self.click_time)

    def fold(self, element: auto.uiautomation.ButtonControl, **kwargs):
        """
        闭合节点操作
        :param element:
        :return:
        """
        if element.GetTogglePattern().ToggleState == 1:
            if kwargs:
                self.logger.info('闭合：{}--选项'.format(kwargs['name']))
                element.Click()
                time.sleep(self.click_time)
            else:
                element.Click()
                time.sleep(self.click_time)

    def clickloop(self, button: auto.uiautomation.ButtonControl, card: auto.uiautomation.ListItemControl,
                  button2: auto.uiautomation):
        """
        循环查找卡号中点击滚动条的操作
        判断卡号是否可点击且判断其可点击y坐标是否超过680（超过则容易引起错误点击）
        :param button: 滚动条组件中的翻页点击按钮
        :param card: 卡号对象
        :param button2: 滚动条组件的单个点击按钮
        :return:
        """
        while card.GetClickablePoint() == (0, 0, False):
            self.logger.info('未找到卡号，点击下一页')
            button.Click()
            time.sleep(self.click_time)

        if card.GetClickablePoint()[1] > 680:
            button2.Click()
            time.sleep(self.click_time)

    # 获得需要执行的案例以及编号
    def read_case_list(self, case_number_sorting):
        """
        从数据表中读取需要执行的案例及其编号
        :param case_number_sorting: 案例执行的顺序
        :return:
        """
        self.logger.info('正在从数据表中读取案例及其编号...')
        file_path = os.getcwd() + r'\data_files\{}.xlsx'.format(self.path_file)
        try:
            file = xlrd.open_workbook(file_path)
        except FileNotFoundError:
            self.logger.error('该文件名不存在，请检查配置文件')
            print('该文件名不存在，请检查配置文件')
            exit(0)

        table = file.sheet_by_index(0)
        rows = table.nrows
        class_change = []

        select_item = ''
        data = []
        for i in range(rows):
            select_item = table.row_values(i)[1]
            if table.row_values(i)[0] not in case_number_sorting:
                select_item = table.row_values(i)[1]
                continue
            if table.row_values(i) not in data:
                self.logger.info('读取案例：{}--成功'.format(table.row_values(i)))
                data.append(table.row_values(i))
                class_change.append(table.row_values(i)[1])

        self.logger.info('读取完毕')
        return data, select_item

    def read_field_data(self):  # 读取案例数据
        """
        从数据表中读取案例数据
        :return:
        """
        self.logger.info('正在从数据表中读取案例数据...')
        file_path = os.getcwd() + r'\data_files\{}.xlsx'.format(self.data_file)
        try:
            file = xlrd.open_workbook(file_path)
        except FileNotFoundError:
            self.logger.error('该文件名不存在，请检查配置文件！')
            print('该文件名不存在，请检查配置文件！')
            exit(0)

        table = file.sheet_by_index(0)
        rows = table.nrows
        fields = table.row_values(0)

        case_ranking = []  # 案例执行顺序
        data_dict = {}  # 需要执行的案例以及相关的字段值
        data_lists = []

        for i in range(1, rows):
            datas = {}
            data_list = table.row_values(i)

            if data_list[1] == 'N':
                continue
            case_ranking.append(data_list[2])
            for data in range(3, len(data_list)):
                datas[fields[0]] = str(data_list[0])
                if data_list[data] != '':
                    datas[fields[data]] = str(data_list[data])
            data_lists.append([data_list[2], datas])
            data_dict[str(data_list[2])] = datas

        data_dict['case_number_sorting'] = case_ranking
        self.logger.info('从数据表中读取案例数据成功')
        return data_dict, data_lists

    def select_menu(self, case, select_item: str, **kwargs):
        """
        选择菜单：
        在认证案例集中菜单为：   1、案例另存为自定义案例集
                            2、银联发出的报文
                            3、银联接收的报文
        在自定义案例集中菜单为：    1、银联发出的报文
                               2、银联接收的报文
                               3、删除案例
        :param case: 需要进行操作的案例
        :param select_item: 菜单选项名称
        :param kwargs: certificate为在认证案例集中使用，custom为在自定义案例集中使用
        :return:
        """

        # 认证案例集中-->CertificationCaseSet
        certification_select_dict = {
            '案例另存为自定义案例集': 0,
            '银联发出的报文': 1,
            '银联接收的报文': 2,
        }

        # 自定义案例集中-->CustomCaseSet
        custom_select_dict = {
            '银联发出的报文': 0,
            '银联接收的报文': 1,
            '删除案例': 2,
        }

        case.DoubleClick()
        self.logger.info('点击：{}'.format(case.Name))
        time.sleep(self.click_time)
        case.RightClick()
        time.sleep(self.click_time)
        select_list = auto.MenuItemControl(ClassName='MenuItem').GetParentControl().GetChildren()

        if 'certification_' in kwargs:
            number = certification_select_dict[select_item]
            selection = select_list[number].TextControl()
            self.logger.info('选择菜单：{}-选项'.format(selection.Name))
            selection.Click()
            time.sleep(self.click_time)
        elif 'custom_' in kwargs:
            number = custom_select_dict[select_item]
            selection = select_list[number].TextControl()
            self.logger.info('选择菜单：{}-选项'.format(selection.Name))
            selection.Click()
            time.sleep(self.click_time)

    def init_left_pane(self):
        """
        默认将滚动条拉到最顶部
        :return:
        """
        self.logger.info('将滚动条拉到顶部')
        pane = auto.PaneControl(ClassName='ScrollViewer')
        if (pane.GetScrollPattern().HorizontalScrollPercent, pane.GetScrollPattern().VerticalScrollPercent) == (
        -1.0, -1.0):
            return
        pane.GetScrollPattern().SetScrollPercent(horizontalPercent=-1, verticalPercent=0.0)

    def comparing(self, path_dict: dict, case_list: list):
        """
        从认证案例集中添加案例后，自定义案例集的案例和从数据表中添加的案例集进行对比，
        看是否缺失所需案例
        :param path_dict:
        :param case_list:
        :return: 若返回True，则表示无案例缺失
                 若返回false_list，则表示有缺失案例
        """
        # print("comparing path_dict", path_dict)
        self.logger.info('正在校验所添加案例是否缺失...')
        know_list = [path_dict[i] for i in path_dict]
        # print("know_list", know_list)
        zdy_list = [case.TextControl().Name for case in case_list]
        false_list = [case for case in know_list if case not in zdy_list]
        if len(false_list) == 0:
            return True
        else:
            self.logger.error('缺失"{}"个案例数, 为：{}'.format(len(false_list), false_list))
            print('缺失"{}"个案例数, 为：{}'.format(len(false_list), false_list))
            return false_list

    def re_add_case(self, path_dict: dict, case_list: list, full_path_list: list):
        """
        通过prepare函数中若得到返回值判断是否使用该函数
        若返回值类型为list：调用该函数重新添加
        若返回值类型为bool：则不调用该函数
        :param path_dict:{案例编号：末路径}
        :param case_list:从自定义案例集获取的案例
        :param full_path_list:从数据表中获取的完整案例
        :return:
        """
        # print("re_add_case path_dict", path_dict)
        # print("re_add_case case_list", case_list)
        self.logger.info('正在重新添加缺失案例...')
        num_list = [path_dict[case] for case in case_list]
        add_list = []
        for num in num_list:
            for path in full_path_list:
                if num == path[0]:
                    add_list.append(path)
        # print("add_list", add_list)
        rz = certification_case_set.CertificationCaseSet(add_list, self.logger)
        rz.add_case_list()
        self.logger.info('重新添加缺失案例：{}'.format(case_list))

    def compare(self, path_dict: dict, original_case_list: list, custom):  # custom.case_list
        """
        通过prepare函数中若得到返回值判断是否使用该函数
        若返回值类型为list：调用该函数重新添加
        若返回值类型为bool：则不调用该函数
        :param path_dict: {案例编号：末路径}
        :param case_list: 从自定义案例集获取的案例
        :return:
        """
        self.logger.info('正在重新添加案例集...')
        false_list = self.comparing(path_dict, custom.case_list)
        # print("false_list", false_list)
        reverse_path = {v: k for k, v in path_dict.items()}
        # print("reverse_path", reverse_path)
        if type(false_list) is list:
            self.re_add_case(reverse_path, false_list, original_case_list)
            self.logger.info('重新添加案例集成功')
        else:
            self.logger.info('无缺失案例')

    def get_f39(self):
        self.logger.info('获取案例技术描述中的F39应答码信息')
        message = auto.GroupControl(Name='案例基本信息').GetChildren()
        message = message[-1].GetLegacyIAccessiblePattern().Value
        message = message.split('\n')
        f39_pat = 'F39=(.+)'
        flag = False
        result_list = []
        for i in message:
            result = re.compile(f39_pat).findall(i)
            if len(result) == 0:
                self.expected_F39.append('00')
                pass
            elif len(result) == 1:
                flag = True
                self.expected_F39.append(result[0])
                result_list = result[0].split('或')
        if flag is False:
            return None
        else:
            return result_list

    # 批量填写报文数据
    def batch_filling(self, data_list: list, path_dict: dict, custom):
        count = 1
        flag = ''  # 用于标记多案例集
        custom.get_case_list()
        custom.click_self()
        error_list = []  # 用于多案例集中，标记案例失败的列表
        field_error = ''

        for number, data_dict in data_list:
            path = path_dict[number]
            # 自定义案例集现存案例
            case_list = custom.case_list
            if len(error_list) > 0:
                if data_dict['案例类型'] == 'cases':
                    count += 1
                    continue
                if data_dict['案例类型'] == 'caseEnd':
                    count += 1
                    error_list.clear()
                    # 要执行一个清空日志的操作
                    tab = auto.TabControl(AutomationId='mainTab').TabItemControl(
                        Name='emd.ViewModel.CustomLogViewModel')
                    self.logger.info('点击日志信息')
                    tab.DoubleClick()
                    clean_button = auto.ButtonControl(ClassName='Button', Name='清空')
                    clean_button.DoubleClick()
                    error_list.append('error')
                    continue

            for case in case_list:
                if path == case.TextControl().Name:
                    auto.PaneControl(ClassName='ScrollViewer').Click()
                    # 自动寻找案例名称
                    case.GetScrollItemPattern().ScrollIntoView()
                    case.TextControl().Click()
                    result = self.get_f39()

                    # 序号
                    num = data_dict['序号']
                    del data_dict['序号']

                    # 面板滑到最左边
                    try:
                        auto.PaneControl(AutomationId='scroll').GetScrollPattern().SetScrollPercent(
                            horizontalPercent=-1, verticalPercent=100)
                    except:
                        pass

                    # 记录案例类型，以及判断是否存在卡号2
                    case_type = data_dict['案例类型']
                    del data_dict['案例类型']
                    select_card = custom.select_card_id(data_dict['卡号1'], '卡号1', num)
                    del data_dict['卡号1']
                    if '卡号2' in data_dict:
                        select_card = custom.select_card_id(data_dict['卡号2'], '卡号2', num)
                        del data_dict['卡号2']

                    # 判断案例所选卡号是否存在
                    if select_card is False:
                        if case_type == 'cases':
                            error_list.append('error')
                            break
                        if case_type == 'caseEnd':
                            error_list.clear()
                            # 要执行一个清空日志的操作
                            tab = auto.TabControl(AutomationId='mainTab').TabItemControl(
                                Name='emd.ViewModel.CustomLogViewModel')
                            self.logger.info('点击日志信息')
                            tab.Click()
                            clean_button = auto.ButtonControl(ClassName='Button', Name='清空')
                            clean_button.Click()
                            error_list.append('error')
                            break
                        break

                    # 发出报文
                    self.select_menu(case.TextControl(), '银联发出的报文', custom_='custom')
                    field_error = ''
                    for field in data_dict:
                        status = custom.edit_field(field, data_dict[field], num)
                        if type(status) is tuple:
                            if status[0] is False:
                                field_error += status[1]
                                break
                    custom.save()
                    custom.execute_case()

                    # 判断是否出现线路断开提示框，如果出现则点掉
                    while auto.WindowControl(Name='提示').Exists(1):
                        auto.WindowControl(Name='提示').SetTopmost()
                        time.sleep(self.click_time)
                        try:
                            auto.ButtonControl(Name='确定').Click()
                        except:
                            pass
                        self.logger.error('案例执行失败，对应案例序号为：{}'.format(num))
                        print('案例执行失败，对应案例序号为：{}'.format(num))

                    auto.WindowControl(Name='中国银联入网测试仿真系统（机构版）').SwitchToThisWindow()

                    if case_type == 'cases' or case_type == 'caseEnd':
                        flag = flag + str(count) + '-'
                    if case_type == 'caseEnd':
                        self.execute_result.append(
                            custom.log_information(num, flag, case_type, result, self.summary_file))
                        flag = ''
                    else:
                        self.execute_result.append(
                            custom.log_information(num, str(count) + '-', case_type, result, self.summary_file))

                    break
            count += 1
            self.failure_reason.append('字段：{}搜索失败'.format(field_error))

        self.summary_log()

    def clean_log(self):
        try:
            tab = auto.TabControl(AutomationId='mainTab').TabItemControl(Name='emd.ViewModel.CustomLogViewModel')
            self.logger.info('点击日志信息')
            tab.DoubleClick()
            clean_button = auto.ButtonControl(ClassName='Button', Name='清空')
            clean_button.DoubleClick()
            self.logger.info('清空界面日志信息')
        except LookupError:
            pass

    def write_result_excel(self):
        self.logger.info('将结果写入Excel表格...')
        self.result_list = self.result_list + ['技术描述F39应答码', '报文检查', '执行结果']
        total = [['案例序号'] + self.result_list] + self.execute_result
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        precise_time = datetime.datetime.now().strftime('%H%M%S')
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('{}'.format(today))

        # 初始化样式，如果案例成功则变绿，否则变红
        style = xlwt.XFStyle()
        success_pat = xlwt.Pattern()
        success_pat.pattern = xlwt.Pattern.SOLID_PATTERN
        success_pat.pattern_fore_colour = 3
        fail_pat = xlwt.Pattern()
        fail_pat.pattern = xlwt.Pattern.SOLID_PATTERN
        fail_pat.pattern_fore_colour = 2

        for i in range(len(total)):
            for j in range(len(total[i])):
                data = total[i][j]
                if j == 0:
                    number = total[i][j]
                if i == 0:
                    worksheet.write(i, j, data)
                elif j == len(total[i]) - 1:
                    if data is True:
                        style.pattern = success_pat
                        worksheet.write(i, j, '成功', style)
                        self.success_case.append(number)
                        del self.undo[self.undo.index(number)]
                    elif data is False:
                        style.pattern = fail_pat
                        worksheet.write(i, j, '失败', style)
                        self.fail_case.append(number)
                        del self.undo[self.undo.index(number)]
                else:
                    worksheet.write(i, j, data)

        path = os.getcwd() + r'\result_files\{}'.format(today)
        if not os.path.exists(path):
            os.makedirs(path)

        workbook.save(path + r'\{}-{}.xls'.format(self.data_file, precise_time))
        self.logger.info('写入成功，该表格仅保存已执行过案例的结果')

    def summary_log(self):
        path = os.getcwd() + r'\log_files\summary_log_files\{}'.format(datetime.datetime.now().strftime('%Y-%m-%d'))
        if not os.path.exists(path):
            os.makedirs(path)
        self.summary_file.save(path + r'\{}-{}.docx'.format(self.data_file, datetime.datetime.now().strftime('%H%M%S')))
        self.logger.info('保存日志汇总')

    def undo_list(self, undo: list):
        self.undo = undo
        self.whole_case = len(self.undo)

    def summary(self):
        print("**********")
        print("程序运行完毕，运行结果如下：")
        print("共有案例-{}-个，执行成功案例-{}-个，执行失败案例-{}-个，未执行案例-{}-个".format(
            self.whole_case, len(self.success_case), len(self.fail_case), len(self.undo)))
        if len(self.fail_case) > 0:
            print("执行失败案例序号为：")
            for number in self.fail_case:
                print(number, end='，')
            print()

        if len(self.undo) > 0:
            print("未执行案例序号为：")
            for number in self.undo:
                print(number, end='，')
            print()
        print("**********")


if __name__ == '__main__':
    pass
