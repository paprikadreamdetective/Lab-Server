from abc import ABC, abstractmethod

class Crud(ABC):
    @abstractmethod
    def init_connection_db(self):
        pass
    @abstractmethod
    def create_experiment(self):
        pass
    @abstractmethod
    def get_experiment(self):
        pass
    @abstractmethod
    def update_experiment(self):
        pass
    @abstractmethod
    def remove_experiment(self):
        pass