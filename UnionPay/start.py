#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from UnionPay.ControlEngine.ControEngine import ControlEngine


def userRun():
    print("*" * 10 + "请输入案例执行的顺序" + "*" * 10)
    print("*" * 10 + "认证案例集输入【1】" + "*" * 11)
    print("*" * 10 + "自定义案例集输入【2】" + "*" * 9)
    print("*" * 10 + "退出运行程序输入【0】" + "*" * 9)
    inputInfo = input("*" * 10 + "请输入你的选择>>>" + "*" * 13 + os.linesep)
    while 1:
        if inputInfo == '1' or inputInfo == '2':
            seconde = input("*" * 10 + "请再次输入你的选择" + "*" * 10 + os.linesep)
            print(f"用户再次输入了{seconde}")
            if inputInfo == seconde:
                print("两次输入一致，程序启动")
                ListResult = ControlEngine().run(inputInfo)
                FailCaseNo = 0
                SuccessfulCaseNo = 0
                FailNum = []
                Successfulnum = []
                print(f"一共执行了{len(ListResult)}条数据")
                for i in range(len(ListResult)):
                    if ListResult[i][-1] is False:
                        FailCaseNo += 1
                    else:
                        SuccessfulCaseNo += 1
                print(f"失败的案例有{FailCaseNo}条")
                caseExeInfo(ListResult, False, "失败", FailNum)
                print(f"成功的案例有{SuccessfulCaseNo}")
                caseExeInfo(ListResult, True, "成功", Successfulnum)
                input("程序运行结束，请按任意键退出")
                return True
            else:
                print("两次输入内容不一致，请重新运行程序")
                exit()
        elif inputInfo == '0':
            print("程序结束")
            exit()
            break


def caseExeInfo(ListResult, isTrue, resultName, Num):
    for i in range(len(ListResult)):
        if ListResult[i][-1] is isTrue:
            pp = ListResult[i][0]
            if pp not in Num:
                Num.append(pp)
                print(f"{resultName}的案例编号为》》》：{ListResult[i][0]}")


userRun()
