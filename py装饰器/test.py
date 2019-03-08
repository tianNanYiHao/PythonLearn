#! /usr/bin/python3

# @File:   test.py
# @Author: tiannanyihao
# @DATE:   2019-03-07
# @TIME:   13:46
# @Software: PyCharm
# @Production:


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 无参装饰器
def needMidleName(func):
    def setMidleName():
        print('midleName = fei')
        func()

    return setMidleName


# 无参装饰器演示
@needMidleName
def createName():
    print('name = liu')


createName()
print('*' * 100+'无参装饰器')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 有参数装饰器


def addMidleName(func):
    def createMidle(firstName, midleName='default'):
        print('midleName = %s' % midleName)
        func(firstName)

    return createMidle


@addMidleName
def addFirstName(firstName):
    print('firstName = %s' % firstName)


# 有参数装饰器使用
addFirstName('liu')
print('*' * 100+'有参装饰器')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 通用装饰器(多参数+返回值)
#

def addFunc(func):
    def addNewFunc(name, title, *args, **kwargs):
        print("=================")
        print(*args)
        print("=================")
        return func(name, title, *args, **kwargs)

    return addNewFunc


@addFunc
def func_01(name, title, *args):
    print('--------------')
    print(name)
    print(title)
    print('--------------')
    return 'abc'


f = func_01('liu', 'fei', 'fei2', 'fei3')
print(f)
print('*' * 100+'通用装饰器(多参数+返回值)')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 多装饰器


def add_func_01(func):
    print('执行了装饰器01')

    def add():
        print('====== 装饰器01 执行了被装饰函数======')
        return func()

    return add


def add_func_02(func):
    print('执行了装饰器02')

    def add():
        print('====== 装饰器02 执行了被装饰函数======')
        return func()

    return add


def add_func_03(func):
    print('执行了装饰器03')

    def add():
        print('====== 装饰器03 执行了被装饰函数======')
        return func()

    return add


@add_func_01
@add_func_02
@add_func_03
def test_01():
    print('----------test1----------')


r = test_01()
print('*' * 100+'多装饰器')
#
# # 执行结果如下:
# # 执行了装饰器03
# # 执行了装饰器02
# # 执行了装饰器01
# # ====== 装饰器01 执行了被装饰函数======
# # ====== 装饰器02 执行了被装饰函数======
# # ====== 装饰器03 执行了被装饰函数======
# # ----------test1----------

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 类装饰器


