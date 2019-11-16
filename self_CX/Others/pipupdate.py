#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

from subprocess import call

from pip._internal.utils.misc import get_installed_distributions


def pythonpacgeUpdate():
    for dist in get_installed_distributions():
        call("pip3 install --upgrade " + dist.project_name, shell=True)


if __name__ == '__main__':
    pythonpacgeUpdate()
