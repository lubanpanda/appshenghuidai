#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import xlrd

"""
1. 读取Excel文件
2. 指定某个数据读取和循环读取
"""


class readFile(object):
    def __init__(self, file_path: str) -> None:
        """
        :param file_path:文件读取路径
        """
        self.fiile_path = file_path

    def open_excel(self) -> xlrd.book.Book:
        try:
            openfile = xlrd.open_workbook(self.fiile_path)
            if openfile:
                print("文件打开成功")
            return openfile
        except FileNotFoundError:
            print("文件路径填写错误，请重新检查")
            exit(0)

    "读取单独的某个内容"

    def read_excle_row_cell(self, sheetIndex: int, row: int, cell: int) -> object:
        """
        :param sheetIndex:sheet索引号
        :param row: 行号
        :param cell: 列号
        :return:
        """
        open_file = self.open_excel()
        if open_file is not False:
            sheet = open_file.sheet_by_index(sheetIndex)
            sheet_info = sheet.cell(row, cell).value
            if sheet_info == "":
                print("诶呀，这是一个空数据填写进去了")
                return None
            else:
                print("数据内容是:" + sheet_info)
                return sheet_info
        else:
            return None

    "循环读取一行数据内容"

    def read_excel_range(self, sheetIndex, rows):
        """
        :param sheetIndex:sheet索引号
        :param rows: 数据的行号
        :return:
        """
        file_name_json = {}
        range_file = self.open_excel()
        if range_file is not False:
            sheet = range_file.sheet_by_index(sheetIndex)
            rows_name = sheet.row_values(0)
            row_name = sheet.row_values(rows)
            for i in range(len(rows_name)):
                file_name_json[rows_name[i]] = row_name[i]
            print(file_name_json)
            return file_name_json
        else:
            return None


if __name__ == '__main__':
    aa = readFile("/Users/panda/Desktop/查询结果的副本.xlsx")
    aa.read_excel_range(0, 1)
