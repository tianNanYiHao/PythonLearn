#! /usr/bin/python3

# @File:   mini_frameDemo.py
# @Author: tiannanyihao
# @DATE:   2019-03-06
# @TIME:   13:56
# @Software: PyCharm
# @Production: 实现一个简单的mini_WEN服务框架


def index():
    return '首页'


def login():
    return '登录页'


# 设置路由
URL_DICT = {
    '/index': index,
    '/login': login,
}


# mini WEB 服务框架入口
# 遵循 WSGI 协议
def application(env, start_response):

    start_response('200 ok', [('Content-Type', 'text/html;charset=utf-8')])
    str = env['path_info']

    try:
        page = URL_DICT[str]
        return page()
    except Exception:
        print('error')
        return '404 not found,再试试别的页面吧!'
