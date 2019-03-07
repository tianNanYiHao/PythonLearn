#! /usr/bin/python3

# @File:   pyBlock.py
# @Author: tiannanyihao
# @DATE:   2019-03-06
# @TIME:   16:15
# @Software: PyCharm
# @Production:


def line(a, b):
    d = 100

    def createA(c):
        nonlocal d
        print(a + b + c + d)
        d = 200
        print(a + b + c + d)

    return createA


l = line(1, 2)
l(3)
