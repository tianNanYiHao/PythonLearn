#! /usr/bin/python3

# @File:   Taobao.py
# @Author: tiannanyihao
# @DATE:   2019-03-01
# @TIME:   11:11
# @Software: PyCharm
# @Production:


from Login import *
from Regist import *
from Buy import *


class Taobao(object):

    def __init__(self):
        """
        模拟App类:
        1.用户登录
        2.用户注册
        3.用户查询商品
        4.用户购物
        5.用户查看订单信息
        6.用户查看订单详情
        """

        self.l = Login()
        self.r = Regist()
        self.b = Buy()
        self.g = Goods()
        self.isLogin = False

        print('------------欢迎进入桃宝------------')

    def startApp(self):

        if self.isLogin:
            print('======= 已登录 ======')
            self.showGoods()
            return

        print('--------您尚未登录,请输入用户名密码登录--------')
        while True:
            name = input('请输入登陆用户名:')
            pwd = input('请输入登陆密码:')

            isSuccess = self.l.login(name, pwd)
            if isSuccess:
                print('******* 恭喜您登陆成功 ********')
                return
            else:
                print('******* 阿欧,您输入的账户名密码有误')
                print('[按1再次输入]')
                print('[按2去注册账户]')
                num = input('请输入命令:')
                if num == '1':
                    self.showGoods()
                    continue
                else:
                    self.regist()
                    return

    def regist(self):

        while True:
            name = input('请输入注册用户名:')
            address = input('请输入收货地址:')
            tel = input('请输入联系手机号:')
            pwd = input('请输入密码:')
            isSuccess = self.r.regist(name, address, tel, pwd)
            if isSuccess:
                print('****** 注册成功,请重新登录 *******')
                self.startApp()
                return
            else:
                print('****** 注册失败 ******')
                print('有账户,重新登录请按1')
                print('无账户,重新注册请按2')
                num = input('请输入命令:')
                if num == '1':
                    self.startApp()
                    return
                else:
                    continue

    def showGoods(self):

        while True:
            print('====== 欢迎进入商品查询系统 =======')
            print('按[1]查询所有商品')
            print('按[2]查询最便宜商品')
            print('按[3]查询最贵商品')
            print('按[4]查询产品类型为笔记本的最便宜商品')
            print('按[5]查询产品类型为台式机的最贵商品')
            num = input('输入命令:')
            print('====== 开始查询 ======  \n')

            if num == '1':
                self.b.showGoods()
            elif num == '2':
                self.b.showPriceMin()
            elif num == '3':
                self.b.showPriceMax()
            elif num == '4':
                self.b.showPriceMinGroupby(1)
            elif num == '5':
                self.b.showPriceMaxGroupby(1)
            else:
                pass
            print('\n======  查询完成 ======  \n')
            print('++++++++++++++ 是否选购以上商品? Y/N ++++++++++++++')
            r = input('请输入Y/N决定是否购买:')
            if r == 'y' or r =='Y':
                self.buyGood()
            elif r == 'n' or r == 'N':
                print('嗯,让我们继续逛逛吧!')
                return





    def buyGood(self):
        print('开始下单.....')
        self.b.buyGood()



if __name__ == '__main__':
    t = Taobao()
    t.startApp()
