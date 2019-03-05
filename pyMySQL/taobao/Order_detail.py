#! /usr/bin/python3

# @File:   Order_detail.py
# @Author: tiannanyihao
# @DATE:   2019-02-28
# @TIME:   16:32
# @Software: PyCharm
# @Production: 订单详情


from SqlHelps import *


class OrdersDetail(object):
    """
    订单详情类
    记录商品信息
    关联订单信息
    1.提供商品信息查询
    """

    def __init__(self):
        self.sql = SqlHelp('taobao')
        pass

    def insert(self, *args):
        pass

    def __del__(self):
        """
        销毁,关闭数据库连接
        :return:
        """
        self.sql.close()
