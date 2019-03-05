#! /usr/bin/python3

# @File:   Goods.py
# @Author: tiannanyihao
# @DATE:   2019-02-28
# @TIME:   14:41
# @Software: PyCharm
# @Production: 商品

from SqlHelps import *


class Goods(object):
    """
    商品信息类
    记录商品品牌
    记录商品型号
    1.提供商品信息数据
    """

    def __init__(self):
        self.sql = SqlHelp('taobao')
        self.sqlStr = None

    def insertDate(self, *args):
        """
        上架新商品
        :param args: 商品名(name),分类(cate_id),品牌(brand_id),价格(price),是否可售,是否卖完
        :return:
        """
        sql = """insert into goods values (0,'%s','%s','%s','%s',default ,default )""" % (
            args[0], args[1], args[2], args[3])

        self.sql.cursor.execute(sql)
        self.sql.con.commit()

    def selectPriceMin(self):
        """
        查询最便宜的商品
        :return:
        """
        sql = """select * from goods where price=(select min(price) from goods) """
        return sql

    def selectPriceMax(self):
        """
        查询最贵的商品
        :param args:
        :return:
        """
        sql = """select * from goods where price=(select max(price) from goods) """
        return sql

    def selectPriceMinGroupBy(self, cateID):
        """
        查询某个分类下,最便宜的商品,价格从小到大排列
        :param cateID:
        :return:
        """
        sql = """select * from goods where cate_id='%s' order by price""" % cateID
        return sql

    def selectPriceMaxGroupBy(self, cateID):
        """
        查询某个分类下,最贵的商品,价格从大到小排列
        :param cateID:
        :return:
        """
        sql = """select * from goods where cate_id='%s' order by price desc""" % cateID
        return sql

    def executForSelect(self, sql):
        """
        执行sql语句-查询类sql语句
        返回 数量及结果对象
        :param sql:
        :return:
        """
        count = self.sql.cursor.execute(sql)
        result = self.sql.cursor.fetchall()
        return count, result

    def selectAll(self):
        return self.sql.selectAll('goods')

    def createOrder(self, userID, goodID):
        # sql_insertOrders = """insert into orders values (default ,"%s","%s")""" % (Date(), userID)

        sql = """select max(id) from * order_detail"""


        # sql_insertOrder_detail = """insert into order_detail values (default ,'%s','%s',default )""" % (?,goodID)


        pass

    def __del__(self):
        """
        销毁,关闭数据库连接
        :return:
        """
        self.sql.close()
