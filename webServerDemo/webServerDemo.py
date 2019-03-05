#! /usr/bin/python3

# @File:   webServerDemo.py
# @Author: tiannanyihao
# @DATE:   2019-01-24
# @TIME:   16:17
# @Software: PyCharm
# @Production:


from socket import *
import re


class HttpServer(object):


    def __init__(self):
        pass




    def runWebServer(self):
        '''
        运行web服务器
        :return:
        '''

        # 启动服务端socket
        tcp_server_socket = socket(AF_INET, SOCK_STREAM)
        # 设置服务器端口可重复使用
        tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        # 绑定服务端socket端口
        tcp_server_socket.bind(('', 10089))
        # 起订服务端socket监听
        tcp_server_socket.listen(128)

        # 工作循环
        while True:
            # 接受客户端socket,地址
            tcp_clien_socket_new, client_add = tcp_server_socket.accept()
            # 调用服务接口服务客户端
            self.workForClient(tcp_clien_socket_new)

        # 关闭服务端服务器
        tcp_server_socket.close()

    def workForClient(self,client_socket):
        '''
        提供客户端相关服务
        :param client_socket:
        :return:
        '''

        # 获取客户端请求数据
        request = client_socket.recv(1024).decode('utf-8')
        print(request)

        # 正则抓取请求数据文件名
        request_arr = request.splitlines()
        ret = re.match(r'[^/]+(/[^ ]*)', request_arr[0])
        if ret:
            fire_name = ret.group(1)

        try:
            fire = open('.' + fire_name, 'rb')
            fire_context = fire.read()
            fire.close()

            # 拼装返回数据格式
            response = 'HTTP/1.1 200 OK\r\n'
            response += '\r\n'
            # 发送返回数据
            client_socket.send(response.encode('utf-8'))
            client_socket.send(fire_context)

        except:
            response = 'HTTP/1.1 404 NOT FOUND\r\n'
            response += '\r\n'
            response += '<p>别找了兄逮, 服务器没你要的数据</p>'
            client_socket.send(response.encode('gb2312'))

        # 关闭客户端服务
        client_socket.close()
        pass


if __name__ == '__main__':
    server = HttpServer()
    server.runWebServer()