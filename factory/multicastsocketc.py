from .socketc import SocketC
import socket as socketUDP
import struct

class MulticastSocket(SocketC):
    def __init__(self, multicast_group, port):
        self.multicast_group = multicast_group
        self.port = port
        self.socket = self.init_connection()
    
    def init_connection(self) -> socketUDP:
        multicast_socket = socketUDP.socket(socketUDP.AF_INET, socketUDP.SOCK_DGRAM)
        multicast_socket.setsockopt(socketUDP.IPPROTO_IP, socketUDP.IP_ADD_MEMBERSHIP, struct.pack('4sL', socketUDP.inet_aton(self.multicast_group), socketUDP.INADDR_ANY))
        return multicast_socket

    def receive_msg(self) -> tuple:
        return self.socket.recvfrom(1024)
