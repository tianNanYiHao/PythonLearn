#! /usr/bin/python3

# @File:   SocketTcpServer.py
# @Author: tiannanyihao
# @DATE:   2019-01-17
# @TIME:   14:02
# @Software: PyCharm
# @Production: tcp的Server服务端,绑定端口10089,接受client端发送的请求,并返回对应的消息!!!


from socket import *


def serverSocket():
    # 1.创建socket-服务端
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    # 2.服务端绑定端口哦号
    tcp_server_socket.bind(('', 10089))
    # 3.服务端监听
    tcp_server_socket.listen(128)

    while True:  # 循环调用,为多个客户端提供服务
        # 4.服务端等待客户端的链接(返回客户端socket,客户端地址)
        new_client_socket, client_address = tcp_server_socket.accept()

        while True:  # 循环调用,为同一个客户端提供服务
            # 5.接受客户端的消息
            recv_data = new_client_socket.recv(1024)
            print('服务端接受到客户端:', new_client_socket, '========>发送的数据:', recv_data)
            if recv_data:
                # 6.给客服端返回消息
                new_client_socket.send('lalalal!!!这是服务端返回消息!!! hello-clien'.encode('utf-8', ))
            else:
                break

        # 7.关闭socket
        new_client_socket.close()

    tcp_server_socket.close()


# 启动
if __name__ == '__main__':
    serverSocket()
