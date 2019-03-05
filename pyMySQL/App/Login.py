#! /usr/bin/python3

# @File:   Login.py
# @Author: tiannanyihao
# @DATE:   2019-03-01
# @TIME:   15:38
# @Software: PyCharm
# @Production:


from User import *


class Login(object):

    def __init__(self):
        self.logName = None
        self.pwd = None

    def login(self, logName, pwd):

        """
        登陆接口
        返回是否登陆成功!
        :param logName:
        :param pwd:
        :return:
        """
        u = User()
        isExist = u.isExistUser(logName)
        if isExist:
            pwd_sql = u.selectPwdByName(logName)
            if pwd == pwd_sql:
                return True
        else:
            return False
