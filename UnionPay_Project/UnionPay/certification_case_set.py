import uiautomation as auto

from UnionPay import common


class CertificationCaseSet:
    def __init__(self, case_list, logger):
        self.certificate = common.Common(logger)
        self.logger = logger
        self.click_self()
        self.pre_case_list = case_list
        self.click_time = self.certificate.click_time

    def click_self(self):
        auto.TabItemControl(Name='认证案例集').DoubleClick()
        self.logger.info('点击认证案例集')

    # 认证案例集-->左下角菜单
    def left_lower_menu(self, menu_item):
        menu_list = auto.ListControl(ClassName='ListView')
        menu_list.DoubleClick()
        menu_list.GetScrollPattern().SetScrollPercent(-1, 0)

        flag = False
        for i in menu_list.GetChildren():
            if i.Name == menu_item:
                flag = True
                i.GetScrollItemPattern().ScrollIntoView()
                i.Click()
                break

        if flag is False:
            self.logger.error('没有路径--{}，请检查路径'.format(menu_item))
            print('没有路径--{}，请检查路径'.format(menu_item))
            input("请按任意键退出。。。")
            exit(0)

    # 闭合所有案例节点
    def fold_all_toggle(self):
        button = auto.ButtonControl(AutomationId='Expander')
        self.certificate.unfold(button, name=button.GetParentControl().TextControl().Name)

        focus = auto.TreeControl(AutomationId='treeView').TreeItemControl().TextControl()
        self.logger.info('点击：{}'.format(focus.Name))
        focus.Click()

        menu_list = auto.TreeItemControl(ClassName='TreeViewItem').GetChildren()
        menu_list = [i for i in menu_list if i.Name == 'emd.ViewModel.SubLevelViewModel']
        for i in menu_list:
            if i.ButtonControl():
                self.certificate.fold(i.ButtonControl(), name=i.TextControl().Name)

    # 搜索案例
    def find_case(self, case_list: list):
        """
        用于搜索案例
        :param case_list: 每次仅传入单条案例路径
        :param seconde:
        :return:
        """

        count = 0
        flag = True
        focus_path = ''
        root = auto.TreeItemControl(Name='emd.ViewModel.SubLevelViewModel').TextControl(Name=case_list[0])
        temp_list = [i for i in root.GetParentControl().GetChildren() if i.Name == 'emd.ViewModel.SubLevelViewModel']
        for path in range(1, len(case_list)):  # 从路径的第二个开始搜索
            for i in temp_list:
                focus_path = case_list[path]
                if i.TextControl().Name == case_list[path]:
                    count += 1
                    i.GetScrollItemPattern().ScrollIntoView()
                    if i.ButtonControl():
                        self.certificate.unfold(i.ButtonControl(), name=i.TextControl().Name)  # 展开该节点下的案例

                        # 获取展开节点的子节点
                        temp_list = [temp for temp in i.GetChildren() if temp.Name == 'emd.ViewModel.SubLevelViewModel']
                        if path == len(case_list) - 1:
                            i.GetScrollItemPattern().ScrollIntoView()
                            i.TextControl().Click()

                            self.certificate.select_menu(i.TextControl(), '案例另存为自定义案例集', certification_='certificate')
                            self.logger.info('添加案例：{}--成功'.format(i.TextControl().Name))

        if count < len(case_list) - 1:
            self.logger.error('案例路径:{}书写错误，未找到该路径，请检查路径文件！'.format(focus_path))
            print('案例路径:{}书写错误，未找到该路径，请检查路径文件！'.format(focus_path))
            input("请按任意键退出。。。")
            exit(0)
        if flag is False:
            self.logger.error('案例路径:{}书写错误，未找到该路径，请检查路径文件！'.format(focus_path))
            print('案例路径:{}书写错误，未找到该路径，请检查路径文件！'.format(focus_path))
            input("请按任意键退出。。。")
            exit(0)

    # 添加案例
    def add_case_list(self):
        self.logger.info('正在添加案例集...')
        auto.TreeControl(ClassName='TreeView').TreeItemControl().TextControl().Click()

        count = 0
        for case in self.pre_case_list:
            # 当count是0，也就是添加第一条案例时，默认寻找左下角路径，否则判断当前路径和上一条路径的左下角路径是否相同
            if count > 0:
                if case[1] != self.pre_case_list[count - 1][1]:
                    # 寻找左下角路径
                    self.left_lower_menu(case[1])
            else:
                self.left_lower_menu(case[1])

            # case[1:] --> ['3', '发卡方-有卡', 'CDM存款业务', 'CDM存款（磁条）', '有卡存款', '1 CDM存款-成功-刷卡无密']
            self.find_case(case[1:])
            count += 1
        self.logger.info('添加案例及成功')
