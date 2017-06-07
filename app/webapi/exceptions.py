#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/12 下午9:46
# @Author  : Matrix
# @Site    : 
# @File    : exceptions.py
# @Software: PyCharm
from app.apizen.exceptions import ApiBaseExceptions


# API 子系统（业务）层级执行结果，以2000开始
class ApiSubExceptions(ApiBaseExceptions):
    empty_result = {'api_code': 2000, 'http_code': 200, 'api_msg': '查询结果为空', 'ex_type': Exception}
    unknown_error = {'api_code': 2001, 'http_code': 500, 'api_msg': '未知异常', 'ex_type': Exception}
    other_error = {'api_code': 2002, 'http_code': 500, 'api_msg': '其它异常', 'ex_type': Exception}
    user_not_exits = {'api_code': 2003, 'http_code': 404, 'api_msg': '用户不存在', 'ex_type': Exception}
    wrong_password = {'api_code': 2004, 'http_code': 400, 'api_msg': '用户名或密码错误', 'ex_type': Exception}

if __name__ == '__main__':
    pass
