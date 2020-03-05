#! /usr/bin/python3

# @File:   readjson.py
# @Author: tiannanyihao
# @DATE:   2019-07-17
# @TIME:   16:15
# @Software: PyCharm
# @Production:


import json

fp = open('./aaa.json')
js = fp.read()
print(js)
fp.close()