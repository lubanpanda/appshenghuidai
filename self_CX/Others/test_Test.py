#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"
import pytest

"""
全能的mark
mark主要用来标记用例,通过不同的标记实现不同的运行策略
主要用途:

标记和分类用例: @pytest.mark.level1
标记用例执行顺顺序pytest.mark.run(order=1) (需安装pytest-ordering)
标记用例在指定条件下跳过或直接失败 @pytest.mark.skipif()/xfail()
标记使用指定fixture(测试准备及清理方法) @pytest.mark.usefixtures()
参数化 @pytest.mark.parametrize
标记超时时间 @pytest.mark.timeout(60) (需安装pytest-timeout)
标记失败重跑次数@pytest.mark.flaky(reruns=5, reruns_delay=1) (需安装pytest-rerunfailures)
"""


@pytest.mark.timeout(60)
def test_panda():
    print("练习test")


if __name__ == '__main__':
    pytest.main(["test_Test.py"])
