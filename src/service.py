from abc import ABC, abstractmethod

from .entity import Areas, Medidas, Elemento


class Service(ABC):
    @abstractmethod
    def area(self, medidas: object, cantidad: int):
        pass

    @abstractmethod
    def material(self, area: Areas, dosificacion_tipo: str, material_tipo: str):
        pass

    @abstractmethod
    def elemento(self, nombre: str, medidas: Medidas, cantidad: int, dosificacion: str, material_tipo: str):
        pass

    @abstractmethod
    def save_ele(self, element: Elemento):
        pass
