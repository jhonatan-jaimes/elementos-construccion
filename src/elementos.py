from src.areas import Areas
from src.medidas import Medidas2D, Medidas3D


class Elemento:
    def __init__(self, nombre: str, cantidad: int, medidas: object, areas: Areas, material: object):
        self.nombre = nombre
        self.cantidad = cantidad
        self.medidas = medidas
        self.areas = areas
        self.material = material

    def json(self):
        pass

