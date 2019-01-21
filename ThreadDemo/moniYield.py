#! /usr/bin/python3

# @File:   moniYield.py
# @Author: tiannanyihao
# @DATE:   2019-01-21
# @TIME:   14:01
# @Software: PyCharm
# @Production:

import time

def call1():
    print('1111111')
    time.sleep(1)
    pass


def call2():
    print('2222222')
    time.sleep(1)
    pass


def domain():
    while True:
        call1()
        call2()
    pass


if __name__ == '__main__':
    domain()
