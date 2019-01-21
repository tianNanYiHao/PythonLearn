#! /usr/bin/python3

# @File:   Tesssst.py
# @Author: tiannanyihao
# @DATE:   2019-01-21
# @TIME:   10:56
# @Software: PyCharm
# @Production:


def newApb(tiems):
    a = 0
    b = 1
    index = 0
    while index < tiems:

        yield a
        a, b = b, a + b
        index += 1


obj = newApb(1200)

while True:
    try:
        tet = next(obj)
        print(tet)
    except Exception as tet:
        break
