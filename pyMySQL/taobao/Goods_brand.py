#! /usr/bin/python3

# @File:   Goods_brand.py
# @Author: tiannanyihao
# @DATE:   2019-02-28
# @TIME:   16:31
# @Software: PyCharm
# @Production: 商品品牌


from SqlHelps import *

class GoodsBrand(object):
    """
    商品品牌类
    1.提供商品品牌查询
    """

    def __init__(self):
        self.sql = SqlHelp('taobao')

    def selectAll(self):
        return self.sql.selectAll('goods_brand')

    def __del__(self):
        """
        销毁,关闭数据库连接
        :return:
        """
        self.sql.close()