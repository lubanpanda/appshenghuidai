#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : panda  
import os
import sys
from ATM.core import main

base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

if __name__ == '__main__':
    main.run()