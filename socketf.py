
from multicastsocketc import MulticastSocket

class SocketFactory:
    @staticmethod
    def create_multicast_socket(self, multicast_group, port) -> MulticastSocket:
        return MulticastSocket(multicast_group, port)