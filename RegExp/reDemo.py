#! /usr/bin/python3

# @File:   reDemo.py
# @Author: tiannanyihao
# @DATE:   2019-01-22
# @TIME:   14:58
# @Software: PyCharm
# @Production:

import re

ret = re.match(r"[1-9]{1,4}==>[a-zA-Z]{1,4}", "2314==>abCC")
print(ret)
print(ret.group())

inp = input('输入您的邮箱:')

ret2 = re.match(r"[0-9a-zA-Z]{4,20}@(163|126|qq)\.com$", inp)

print(ret2)
