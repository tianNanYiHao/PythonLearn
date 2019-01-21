#! /usr/bin/python3

# @File:   Collections.py
# @Author: tiannanyihao
# @DATE:   2019-01-18
# @TIME:   17:03
# @Software: PyCharm
# @Production: 迭代器.及知道迭代器的用途意义!

from collections import *


class Classmate(object):

    def __init__(self):
        self.names = list()
        self.index = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.names):
            name = self.names[self.index]
            self.index += 1
            return name
        else:
            raise StopIteration


if __name__ == '__main__':

    classMate = Classmate()
    classMate.add('liu')
    classMate.add('fei')
    classMate.add('fei')

    for name in classMate:
        print(name)
