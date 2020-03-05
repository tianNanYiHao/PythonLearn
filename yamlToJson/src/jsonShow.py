#! /usr/bin/python3

# @File:   jsonShow.py
# @Author: tiannanyihao
# @DATE:   2019-07-17
# @TIME:   14:29
# @Software: PyCharm
# @Production:


import json
import re

fp = open('./orig.json')
print(fp)
info = json.load(fp)

with open('./aaa.json', "w+") as writefp:
    arr = []
    for item in info:
        jsonData = item["_source"]["layers"]["data"]['data.data']
        dataArr = re.split(":", jsonData)
        data16_To10_Arr = []
        for itemSub in dataArr:
            number = int(itemSub, 16)
            data16_To10_Arr.append(number)
            pass
        # 组装json
        jsObj = {"data": data16_To10_Arr}
        arr.append(jsObj)
        pass

    print(arr)
    jsstring = json.dumps(arr)
    writefp.write(jsstring)
fp.close()
