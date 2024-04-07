from connectionf import ConnectionF
from multicastsocketc import MulticastSocket

class MulticastSocketFactory(ConnectionF):
    def create_socket(self, multicast_group, port):
        return MulticastSocket(multicast_group, port)