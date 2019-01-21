#! /usr/bin/python3

# @File:   greenletDemo.py
# @Author: tiannanyihao
# @DATE:   2019-01-21
# @TIME:   14:22
# @Software: PyCharm
# @Production:


import gevent
import time


def print1():
    for i in range(10):
        print('llllllll')
        gevent.sleep(1)


def print2():
    for i in range(10):
        print('22222222')
        gevent.sleep(1)
        print(gevent.config)

def print3():
    for i in range(100):
        print('kkkkkkkk')
        gevent.sleep(1)


if __name__ == '__main__':
    g1 = gevent.spawn(print1)
    g2 = gevent.spawn(print2)
    g3 = gevent.spawn(print3)
    g1.join()
    g2.join()
    g3.join()




