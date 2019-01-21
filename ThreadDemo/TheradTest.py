#! /usr/bin/python3

# @File:   TheradTest.py
# @Author: tiannanyihao
# @DATE:   2019-01-17
# @TIME:   15:48
# @Software: PyCharm
# @Production:


import time
import threading

g_num = 100
lock = threading.Lock()


def call1():
    for i in range(5):
        time.sleep(1)
        print('11111')
    print(threading.current_thread())


def call2():
    for i in range(5):
        time.sleep(1)
        print('22222')
    print(threading.current_thread())


def addOne(*args):
    global g_num
    lock.acquire()
    for i in range(args[0]):
        g_num += 1
    lock.release()
    print(threading.current_thread(), '>>>>>>>', g_num)


def printOne(*args):
    global g_num
    lock.acquire()
    for i in range(args[0]):
        g_num += 1
    lock.release()
    print(threading.current_thread(), '=======', g_num)


if __name__ == '__main__':
    t1 = threading.Thread(target=addOne, args=(100000000,))
    t2 = threading.Thread(target=printOne, args=(100000000,))

    t1.start()
    t2.start()

    time.sleep(30)
    print(threading.current_thread(), '00000000', g_num)

    pass


