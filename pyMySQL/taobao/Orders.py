#! /usr/bin/python3

# @File:   Orders.py
# @Author: tiannanyihao
# @DATE:   2019-02-28
# @TIME:   16:31
# @Software: PyCharm
# @Production: 订单信息

from SqlHelps import *


class Orders(object):
    """
    订单类
    记录用户信息
    关联用户详情信息
    1.提供下单数据记录功能
    """

    def __init__(self):
        self.sql = SqlHelp('taobao')

    def insert(self, *args):
        pass

    def __del__(self):
        """
        销毁,关闭数据库连接
        :return:
        """
        self.sql.close()
