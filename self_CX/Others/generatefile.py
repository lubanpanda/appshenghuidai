#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import os


def Writefile():
    file_name = input("请输入要生成的文本文件名字:" + os.linesep)
    file_size = input("请输入文件大小:单位（M）" + os.linesep)
    file_path = os.getcwd() + os.sep + file_name + ".txt"
    if not os.path.exists(file_path):
        with open(file_path, "w"):
            print("正在创建文件中")
    with open(file_path, "w") as f:
        f.write(str("a" * 1024 * 1024 * int(file_size)))


if __name__ == '__main__':
    Writefile()
