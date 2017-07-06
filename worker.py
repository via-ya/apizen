#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2017/7/6 下午9:18
# @Author: BlackMatrix
# @Site: https://github.com/blackmatrix7
# @File: worker
# @Software: PyCharm
import sys
from app import create_app
from app.extensions import celery
__author__ = 'blackmatix'

# command line env
# if sys.argv and len(sys.argv) >= 1 and '-env' in sys.argv[1]:
#     app_config = sys.argv[1][sys.argv[1].find('=') + 1:]
# else:
#     app_config = None

flask_app = create_app('devcfg')

if __name__ == '__main__':
    with flask_app.app_context():
        celery.start()

