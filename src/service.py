from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    def area(self, medidas: object, cantidad: int):
        pass

    @abstractmethod
    def concreto(self, medidas: object, cantidad: int, dosificacion_tipo: str):
        pass

    @abstractmethod
    def mortero(self, medidas: object, cantidad: int, dosificacion_tipo: str):
        pass

    @abstractmethod
    def elemento(self):
        pass
