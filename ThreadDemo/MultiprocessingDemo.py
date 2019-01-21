#! /usr/bin/python3

# @File:   MultiprocessingDemo.py
# @Author: tiannanyihao
# @DATE:   2019-01-18
# @TIME:   16:14
# @Software: PyCharm
# @Production:

from multiprocessing import *


def multiprocessDown(*args):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for data in arr:
        args[0].put(data)


def multiprocessWrit(*args):
    while True:
        data = args[0].get()
        print(data)
        if args[0].empty():
            print('over~')
            break
    pass


def doMain():
    q = Queue()
    multi_down = Process(target=multiprocessDown, args=(q,))
    multi_Write = Process(target=multiprocessWrit, args=(q,))

    multi_down.start()
    multi_Write.start()



if __name__ == '__main__':
    doMain()
