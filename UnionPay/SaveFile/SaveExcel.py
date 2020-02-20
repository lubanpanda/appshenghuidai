#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import datetime
import os

import xlwt


def SaveExcel(data_file, result_list, execute_result):
    # self.logger.info('将结果写入Excel表格...')
    result_list = result_list + ['F39应答码', '报文检查', '执行结果']
    total = [['案例序号'] + result_list] + execute_result
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
                if data is False:
                    style.pattern = fail_pat
                    worksheet.write(i, j, '成功', style)
                    # self.success_case.append(number)
                    # del self.undo[self.undo.index(number)]
                elif data:
                    style.pattern = success_pat
                    worksheet.write(i, j, '失败', style)
                    # self.fail_case.append(number)
                    # del self.undo[self.undo.index(number)]
            else:
                worksheet.write(i, j, data)

    paths = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = paths + r'\result_files\excel_files\{}'.format(today)
    if not os.path.exists(path):
        os.makedirs(path)

    workbook.save(path + r'\{}-{}.xls'.format(data_file, precise_time))
    # self.logger.info('写入成功，该表格仅保存已执行过案例的结果')
