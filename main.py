from socketf import SocketFactory

def main():
    multicast_socket_receiver = SocketFactory.create_multicast_socket('224.10.10.10', '10000')
    while True:
        data, address = multicast_socket_receiver.receive_msg()

if __name__ == "__main__":
    main()



