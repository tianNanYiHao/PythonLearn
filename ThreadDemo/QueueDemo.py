#! /usr/bin/python3

# @File:   QueueDemo.py
# @Author: tiannanyihao
# @DATE:   2019-01-18
# @TIME:   16:01
# @Software: PyCharm
# @Production:


from socket import *
from multiprocessing import *
from threading import *


def queueu():
    q = Queue(4)
    q.put('1')
    q.put('2')
    q.put('3')

    print(q.full())
    q.put('4')
    print(q.full())

    getQueue(q, False)


def getQueue(param, wait=False):
    if wait == True:
        for i in range(10):
            value = param.get()
            print(value)
            if not value:
                print('empty!!!!!!')
    else:
        for i in range(10):
            value = param.get_nowait()
            print(value)
            if not value:
                print('empty!!!!!!')


if __name__ == '__main__':
    queueu()
