#! /usr/bin/python3

# @File:   Regist.py
# @Author: tiannanyihao
# @DATE:   2019-03-01
# @TIME:   15:38
# @Software: PyCharm
# @Production:

from User import *


class Regist(object):

    def __init__(self):
        pass

    def regist(self, name, address, tel, pwd):
        """
        注册插入用户数据
        返回是否插入成功标识
        :param name:
        :param address:
        :param tel:
        :param pwd:
        :return:
        """
        u = User()
        insertSuccess = u.insertData(name, address, tel, pwd)
        return insertSuccess
