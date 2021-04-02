import socket

def main():
    #　创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #可以使用套接字收发数据
    udp_socket.sendto(b"hhhhhhhhh", ("192.168.3.5", 8080))
    
    #关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
