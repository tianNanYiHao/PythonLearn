#! /usr/bin/python3

# @File:   SocketTcpClient.py
# @Author: tiannanyihao
# @DATE:   2019-01-17
# @TIME:   14:03
# @Software: PyCharm
# @Production:  tcp模拟client端向server端发送请求, 模拟回环地址127.0.0.1,server端口10089

from socket import *


def clientSocket():
    # 1.创建socket-客户端
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)

    print('*' * 50, '创建一个新的客户端', '*' * 50)

    server_Ip = input('请输入服务器ip:')
    server_port = input('请输入服务器端口号:')
    if server_Ip == '1':
        server_Ip = '127.0.0.1'
    if server_port == '2':
        server_port = '10089'

    # 2.链接服务器
    tcp_client_socket.connect((server_Ip, int(server_port)))

    while True:
        # 3.用户输入发送的数据
        send_Data = input('请输入要发送的内容:')
        tcp_client_socket.send(send_Data.encode('utf-8'))

        # 4.接受对方发送的数据
        recv_data = tcp_client_socket.recv(1024)
        print('==>接收到服务器返回的消息:', recv_data.decode('utf-8'))
        print('...')
        print('=' * 30, '通信完成,是否继续通信? [1]是,[2]关闭')
        isClose = input('请输入你的决定:')
        if isClose == '1':
            continue
        elif isClose == '2':
            break

    # 5.关闭socket
    tcp_client_socket.close()

    # 6.重新启动一个新的客户端
    clientSocket()


if __name__ == '__main__':
    clientSocket()
