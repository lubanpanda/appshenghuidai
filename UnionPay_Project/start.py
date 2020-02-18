import configparser
import datetime
import os

import loguru
import uiautomation as auto
from UnionPay.certification_case_set import CertificationCaseSet
from UnionPay.common import Common
from UnionPay.custom_case_set import CustomCaseSet


def run():
    logger = loguru.logger
    logger.remove(handler_id=None)
    logger.add(os.getcwd() + r'\log_files\Day_log_files\{}.log'.format(datetime.datetime.now().strftime('%Y-%m-%d')),
               encoding='utf-8')
    while True:
        print('以认证案例集为入口请输入数字--1\n以自定义案例集为入口请输入数字--2\n退出输入数字--0\n')
        choice = input('请输入您的选择：\n')
        print('用户输入：{}'.format(choice))
        if choice == '1' or choice == '2':
            seconde = input('请再次输入您的选择：\n')
            print('用户再次输入：{}'.format(seconde))
            if choice == seconde:
                print('用户两次输入一致，程序启动')
                break
            else:
                print('两次输入不一致，请重新运行程序\n')
                exit(0)
        elif choice == '0':
            print('程序结束')
            exit(0)
        else:
            print('请重新输入您的选择\n')

    auto.WindowControl(Name='中国银联入网测试仿真系统（机构版）').SwitchToThisWindow()
    auto.WindowControl(Name='中国银联入网测试仿真系统（机构版）').Maximize()

    conf = configparser.ConfigParser()
    conf.read(os.getcwd() + r'\settings\config.ini', encoding='utf-8')

    auto.SetGlobalSearchTimeout(float(conf.get('time_config', 'set_global_timeout')))
    common = Common(logger)

    # 先读取案例编号，并获取对应案例数据
    data_dict, data_lists = common.read_field_data()  # 需执行的案例及其字段、数据
    case_sorting = data_dict['case_number_sorting']  # 需执行的案例顺序

    # 根据案例编号，读取案例路径，并添加案例到自定义案例集
    case_list, select_item = common.read_case_list(case_sorting)  # 获取需要添加的案例路径
    # print(case_list)
    # exit(0)

    path_dict = {}  # {案例编号：末路径}
    for path in case_list:
        path_dict[path[0]] = path[-1]
    # print("path_dict", path_dict)

    path_dict1 = {}
    for path in case_list:
        path_dict1[path[0]] = path[-2:]
    # print("path_dict1", path_dict1)

    common.undo_list([data['序号'] for _, data in data_lists])

    logger.info('初始化完毕')
    if choice == '1':
        custom = CustomCaseSet(logger)  # 初始化自定义案例集
        custom.click_self()
        custom.empty_case_list()  # 清空自定义案例集
        certification = CertificationCaseSet(case_list, logger)  # 初始化认证案例集
        certification.add_case_list()  # 添加案例集

        custom.click_self()  # 切换到自定义案例集
        custom.get_case_list()
        common.compare(path_dict, case_list, custom)  # 对比自定义案例集中的案例是否完整
        custom.click_self()
        common.clean_log()
        try:
            common.batch_filling(data_lists, path_dict, custom)  # 批量填写报文数据
        except:
            pass
        finally:
            common.write_result_excel()
            common.summary_log()
    elif choice == '2':
        custom = CustomCaseSet(logger)  # 初始化自定义案例集
        custom.click_self()
        custom.get_case_list()
        common.compare(path_dict, case_list, custom)  # 对比自定义案例集中的案例是否完整
        custom.click_self()
        common.clean_log()
        try:
            common.batch_filling(data_lists, path_dict, custom)  # 批量填写报文数据
        except:
            pass
        finally:
            common.write_result_excel()
            common.summary_log()

    common.summary()
    input("请按任意键退出。。。")
    exit(0)


if __name__ == '__main__':
    run()
