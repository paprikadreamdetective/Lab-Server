'''
Interfaz para el tipo socket:

El proposito de proporcionar una
interfaz llamada 'socket' es para permitir
agregar nuevos tipos de sockets, por ejemplo, sockets udp, websockets.

'''
from abc import ABC, abstractmethod

class SocketC(ABC):
    @abstractmethod
    def init_connection(self):
        pass
    @abstractmethod
    def receive_msg(self):
        pass
