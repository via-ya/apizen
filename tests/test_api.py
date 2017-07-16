#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2017/7/16 21:15
# @Author  : BlackMatrix
# @Site : 
# @File : test_api.py
# @Software: PyCharm
import unittest
import requests
__author__ = 'blackmatrix'


class FlaskTestCase(unittest.TestCase):
    @property
    def request_url(self):
        return '{host}?v={version}&method={method}'.format(
            host=self.api_host, version=self.api_version,  method=self.api_method)

    def setUp(self):
        self.api_host = 'http://127.0.0.1:8080/api/router/rest'
        self.api_version = '1.0'
        self.api_method = 'matrix.api.first-api'

    # 测试第一个接口
    def test_first_api(self):
        self.api_method = 'matrix.api.first-api'
        resp = requests.get(self.request_url)
        assert resp.status_code == 200
        data = resp.json()
        assert '这是第一个Api例子' in data['respone']

    # 测试参数缺失
    def test_missing_args(self):
        self.api_method = 'matrix.api.register_user'
        resp = requests.get(self.request_url)
        assert resp.status_code == 400
        data = resp.json()
        assert '缺少方法所需参数：name' == data['meta']['message']

    # 测试参数默认值
    def test_default_arg_value(self):
        self.api_method = 'matrix.api.register_user'
        playload = {'name': 'tom', 'age': 19.1}
        resp = requests.get(self.request_url, params=playload)
        assert resp.status_code == 200
        data = resp.json()
        assert data['response']['email'] is None

    # 测试错误的参数类型
    def test_error_arg_type(self):
        self.api_method = 'matrix.api.register_user_plus'
        playload = {'name': 'tom', 'age': 19.1, 'birthday': '2007/12/31'}
        resp = requests.get(self.request_url, params=playload)
        assert resp.status_code == 400
        data = resp.json()
        assert '参数类型错误：age <Integer>' == data['meta']['message']



if __name__ == '__main__':
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)