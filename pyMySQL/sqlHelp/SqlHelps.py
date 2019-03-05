#! /usr/bin/python3

# @File:   SqlHelps.py
# @Author: tiannanyihao
# @DATE:   2019-03-01
# @TIME:   11:13
# @Software: PyCharm
# @Production:sql公共类

from pymysql import *


class SqlHelp(object):
    """
    连接数据库的工具类
    返回connect对象及 cursor游标对象
    提供简单的全表数据查询功能
    提供关闭数据库连接的功能
    """

    def __init__(self, database, host='localhost', port=3306, user='root', password='mysql123', charset='utf8'):
        """
        初始化
        :param database: 数据库名
        :param host: 地址
        :param port: 端口
        :param user: 用户名
        :param password: 密码
        :param charset: utf8
        """
        self.con = NULL
        self.cursor = NULL

        self.host = host
        self.database = database
        self.port = port
        self.user = user
        self.password = password
        self.charset = charset
        self.connect()

    def connect(self):
        """
        链接数据库
        :return:
        """
        self.con = connect(host=self.host, port=self.port, user=self.user, database=self.database,
                           password=self.password, charset=self.charset)
        self.cursor = self.con.cursor()

    def selectAll(self, table):
        """
        查询该表下所有数据
        :param table: 表名
        :return: count,result
        """
        count = self.cursor.execute('select * from %s' % table)
        result = self.cursor.fetchall()
        return count, result

    def close(self):
        """
        关闭连接,且清除
        :return:
        """
        self.cursor.close()
        self.con.close()
        self.cursor = NULL
        self.con = NULL
