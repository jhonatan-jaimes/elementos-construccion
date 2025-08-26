from abc import ABC, abstractmethod
from .areas import Areas


class Service(ABC):
    @abstractmethod
    def area(self, medidas: object, cantidad: int):
        pass

    @abstractmethod
    def material(self, area: Areas, dosificacion_tipo: str, cantidad_tipo: str):
        pass

    @abstractmethod
    def elemento(self, nombre: str, medidas: object, cantidad: int, dosificacion_tipo: str, cantidad_tipo: str):
        pass
