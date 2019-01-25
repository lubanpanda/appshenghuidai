#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

import socket

hostname = socket.gethostname()
name = socket.gethostbyname(hostname)
print(name)
input('按任意键退出')
