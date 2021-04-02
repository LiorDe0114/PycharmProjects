#coding=utf-8

from socket import *
def main():
    # 1.创建套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    # 2.绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
    local_addr = ('', 8081) #ip地址和端口号，ip一般不用写，表示本地的任何一个ip
    udp_socket.bind(local_addr)

    # 3.等待接收对方发送的数据
    recv_data = udp_socket.recvfrom(1024) #1024表示本次接收的最大字节数
    recv_msg = recv_data[0]  # 存储接收的数据
    send_addr = recv_data[1]  # 存储发送方的地址信息
    # 4.显示接收到的数据
    #print(recv_data[0].decode('gbk'))
    print("%s:%s" % (str(send_addr), recv_msg.decode("gbk")))
    # 5.关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()