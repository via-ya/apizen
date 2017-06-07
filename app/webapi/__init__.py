#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/28 21:47
# @Author  : BlackMatrix
# @Site    : https://github.com/blackmatrix7
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Blueprint

import app.apizen.version
from app.webapi.methods import ApiMethodsBase, ApiMethodsV10, ApiMethodsV11

__author__ = 'blackmatix'
# 蓝图注册
webapi = Blueprint('webapi', __name__)
# Web Api 版本注册
app.apizen.version.register(ApiMethodsBase, ApiMethodsV10, ApiMethodsV11)

# 必须注册完蓝图后才能导入
from app.webapi import routing

if __name__ == '__main__':
    pass
