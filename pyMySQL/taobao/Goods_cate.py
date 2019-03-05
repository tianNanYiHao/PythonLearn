#! /usr/bin/python3

# @File:   Goods_cate.py
# @Author: tiannanyihao
# @DATE:   2019-02-28
# @TIME:   16:31
# @Software: PyCharm
# @Production: 商品类型


from SqlHelps import *


class GoodsCate(object):
    """
    商品类型类
    1.提供商品类型查询

    """

    def __init__(self):
        self.sql = SqlHelp('taobao')

    def selectAll(self):
        return self.sql.selectAll('goods_cate')

    def __del__(self):
        """
        销毁,关闭数据库连接
        :return:
        """
        self.sql.close()
