#! /usr/bin/python3

# @File:   mini_frameDemo.py
# @Author: tiannanyihao
# @DATE:   2019-03-06
# @TIME:   13:56
# @Software: PyCharm
# @Production: 实现一个简单的mini_WEN服务框架


"""
通过装饰器 自动设置路由进行调用
原理:
当程序执行到 @addRoute 后, 首先调用addRoute()传递url且保存在闭包当中,
返回addRouteFunc引用后,触发函数列表添加func函数操作,然后执行完毕, 即准备完毕,等待真正的func(此处doFunc)调用!
"""

URL_DICT = dict()


# 关联路由的装饰器方法
def addRoute(url):
    def addRouteFunc(func):
        URL_DICT[url] = func  # 此处让空字典添加一条 key=url, value=func引用的 键值对

        def doFunc():
            func()
            return doFunc

    return addRouteFunc


@addRoute("/index")
def index():
    return '首页'


@addRoute("/login")
def login():
    return '登录页'


# mini WEB 服务框架入口
# 遵循 WSGI 协议
def application(env, start_response):
    start_response('200 ok', [('Content-Type', 'text/html;charset=utf-8')])
    str = env['path_info']

    try:
        func = URL_DICT[str]
        return func()
    except Exception as ret:
        return  '404 not found , 没啥资源可以提供的'
