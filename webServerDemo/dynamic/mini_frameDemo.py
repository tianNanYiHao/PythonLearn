#! /usr/bin/python3

# @File:   mini_frameDemo.py
# @Author: tiannanyihao
# @DATE:   2019-03-06
# @TIME:   13:56
# @Software: PyCharm
# @Production:


def application(env, start_response):
    start_response('200 ok', [('Content-Type', 'text/html;charset=utf-8')])

    str = env['path_info']

    if str == '/index':
        return index()
    elif str == '/login':
        return login()
    else:
        return '404: hello word , 我爱中国!'


def index():
    return '首页'


def login():
    return '登录页'
