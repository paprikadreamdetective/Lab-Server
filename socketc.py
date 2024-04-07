'''
Interfaz para el tipo de pokemon:

El proposito de proporcionar una
interfaz llamada 'Type' es para permitir
agregar nuevos tipos de de Pokemon.

'''
from abc import ABC, abstractmethod

class SocketC(ABC):
    @abstractmethod
    def receive_msg(self):
        pass
