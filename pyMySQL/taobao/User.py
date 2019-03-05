#! /usr/bin/python3

# @File:   User.py
# @Author: tiannanyihao
# @DATE:   2019-02-28
# @TIME:   16:32
# @Software: PyCharm
# @Production:


from SqlHelps import *


class User(object):
    """
    用户功能类:
    关联订单
    1.提供用户信息验证功能
    2.提供用户信息录入功能
    3.提供用户信息查询功能
    """

    def __init__(self):
        self.name = None
        self.address = None
        self.tel = None
        self.password = None

        # 连接数据库
        self.sql = SqlHelp('taobao')

    def insertData(self, name, address, tel, password):
        """
        向 user 表 中插入用户信息数据,插入完成关闭连接
        :param name:
        :param address:
        :param tel:
        :param password:
        :return:
        """
        isExist = self.isExistUser(name)
        if isExist:
            print('该用户已存在,请勿重复注册!')
            return False

        self.name = name
        self.address = address
        self.tel = tel
        self.password = password

        sql = """insert into user values(%d,'%s','%s','%s','%s')""" % (
            0, self.name, self.address, self.tel, self.password)

        self.sql.cursor.execute(sql)
        self.sql.con.commit()
        return True

    def selectAll(self):
        """
        查询 user 表 全表数据
        :return:
        """
        return self.sql.selectAll('user')

    def selectPwdByName(self, name):
        """
        通过用户查询用户密码
        :param name:
        :return:
        """
        isExist = self.isExistUser(name)
        if isExist:
            sql_findPwd = """select password from user where name='%s'""" % (name)
            count = self.sql.cursor.execute(sql_findPwd)
            result = self.sql.cursor.fetchone()
            return result[0]

    def isExistUser(self, name):
        """
        检测用户名是否存在
        :param name:
        :return:
        """
        sql_findName = """select name from user where name='%s'""" % (name)
        findName_count = self.sql.cursor.execute(sql_findName)
        if findName_count > 0:
            return True
        return False

    def __del__(self):
        """
        销毁,关闭数据库连接
        :return:
        """
        self.sql.close()
