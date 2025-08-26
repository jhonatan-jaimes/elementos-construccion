from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    def areas(self, medidas: object, cantidad: int):
        pass

    @abstractmethod
    def concreto(self):
        pass

    @abstractmethod
    def mortero(self):
        pass

    @abstractmethod
    def elemento(self):
        pass
