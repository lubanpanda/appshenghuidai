#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import os

import xlwt


def SaveExcel(data_file, result_list, execute_result):
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
                    worksheet.write(i, j, '失败', style)

                else:
                    style.pattern = success_pat
                    worksheet.write(i, j, '成功', style)
            else:
                worksheet.write(i, j, data)

    path = os.getcwd() + r'\result_files\excel_files\{}'.format(today)
    if not os.path.exists(path):
        os.makedirs(path)

    workbook.save(path + r'\{}-{}.xls'.format(data_file, precise_time))
