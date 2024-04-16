from factory.socketf import SocketFactory
from persistence.crudmongodb import crudMongoDB
# Hola mundo
def main():
    multicast_socket_receiver = SocketFactory.create_multicast_socket('224.10.10.10', 10000)
    #db = crudMongoDB('localhost', 27017)
    while True:
        print('Waiting to Receive Message')
        data, address = multicast_socket_receiver.receive_msg()
        print('Received {} bytes from {}'.format(len(data), address))
        print(data)
        #db.create_experiment()
if __name__ == '__main__':
    main()



