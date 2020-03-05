#! /usr/bin/python3

# @File:   yaml2jsonb.py
# @Author: tiannanyihao
# @DATE:   2019-07-16
# @TIME:   22:51
# @Software: PyCharm
# @Production:


import yaml
from yaml import load
import json

fp = open("./2.yaml")
cc = fp.read()

content2 = yaml.load_all(cc, Loader=yaml.FullLoader)
print(content2)

for item in content2:
    for subItem in item:
        print(subItem)
        print(item[subItem])

fp.close()


