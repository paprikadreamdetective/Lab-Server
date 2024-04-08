from factory.socketf import SocketFactory

# Hola mundo
def main():
    multicast_socket_receiver = SocketFactory.create_multicast_socket('224.10.10.10', 10000)
    while True:
        print('Waiting to Receive Message')
        data, address = multicast_socket_receiver.receive_msg()
        print('Received {} bytes from {}'.format(len(data), address))
        print(data)
if __name__ == "__main__":
    main()



