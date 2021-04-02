import socket

def send_msg(socket):
    """发送消息"""
    dest_ip = input("请输入对方的IP:")
    dest_port = int(input("请输入对方的端口号:"))
    send_data = input("请输入要发送的消息：")
    socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

def recv_msg(socket):
    """接收消息并打印"""
    # 接收并显示
    recv_data = socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))


def main():
    #　创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind(("",7788))

    #循环来进行处理事情
    while True:
        # 发送
        send_msg(udp_socket)

        #接收并显示
        recv_msg(udp_socket)


if __name__ == "__main__":
    main()