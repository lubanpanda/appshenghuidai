#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"
"""
打包成双击可执行的Mac文件程序

"""
import os
import shutil

'获取用户输入的文件路径'


def _Path():
    user_path = input('请输入你要打包程序的路径:' + os.linesep)
    for root, dirs, files in os.walk(os.curdir):
        if user_path in files:
            return user_path
        else:
            print('输入的路径不在此处或输入不正确，请手动输入完整路径:' + +os.linesep)
            new_path = input()
            return new_path


def Uninx():
    os.system(f'pyinstaller -F {_Path()}')
    All = os.listdir(os.curdir)
    if 'build' in All:
        shutil.rmtree(os.getcwd() + '/build')
    for i in All:
        if i.endswith('.spec'):
            os.remove(i)


if __name__ == '__main__':
    Uninx()
    print('程序打包成功，所得的打包程序在dist目录下，无用的目录已经呗删除')
