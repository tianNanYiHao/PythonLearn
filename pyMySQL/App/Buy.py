#! /usr/bin/python3

# @File:   Buy.py
# @Author: tiannanyihao
# @DATE:   2019-03-01
# @TIME:   15:38
# @Software: PyCharm
# @Production:


from Goods import *
from Goods_cate import *
from Goods_brand import *


class Buy(object):

    def __init__(self):
        self.g = Goods()
        pass

    def showGoods(self):
        """
        展示所有商品
        :return:
        """
        count, result = self.g.selectAll()

        for i in range(count):
            item = result[i]
            itemm = (item[0], item[1], item[4])
            print(itemm)

    def showPriceMin(self):
        """
        展示最便宜商品
        :return:
        """
        sql = self.g.selectPriceMin()
        self.excuteSql(sql)

    def showPriceMax(self):
        """
        展示最贵商品
        :return:
        """
        sql = self.g.selectPriceMax()
        self.excuteSql(sql)

    def showPriceMinGroupby(self, param):
        """
        展示某个分类下最便宜商品
        :param args:
        :return:
        """
        sql = self.g.selectPriceMinGroupBy(param)
        self.excuteSql(sql)

    def showPriceMaxGroupby(self, param):
        """
        展示某个分类下最贵商品
        :param args:
        :return:
        """
        sql = self.g.selectPriceMaxGroupBy(param)
        self.excuteSql(sql)

    def excuteSql(self, sql):
        """
        执行sql,返回查询数据
        :param sql:
        :return:
        """
        contu, result = self.g.executForSelect(sql)

        for i in range(contu):
            item = result[i]
            itemm = (item[0], item[1], item[4])
            print(itemm)
        return itemm

    def buyGood(self):

        pass

    def createOrder(self):
        pass
