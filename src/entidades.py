from .materiales import Concreto, Mortero
from .medidas import Medidas2D, Medidas3D


class Areas:
    def __init__(self):
        self.area_one = 0.0
        self.area_all = 0.0

    def json(self):
        return {
            "areaUnidad": self.area_one,
            "areaTotal": self.area_all
        }


class Elemento:
    def __init__(self, nombre: str = "", cantidad: int = 0, medidas: object = None,
                 areas: Areas = None, material: object = None):
        self.nombre = nombre
        self.cantidad = cantidad
        self.medidas = medidas
        self.areas = areas
        self.material = material

    def json(self):
        if isinstance(self.medidas, Medidas2D or Medidas3D) and isinstance(self.material, Concreto or Mortero):
            return {
                "nombre": self.nombre,
                "cantidad": self.cantidad,
                "medidas": self.medidas.json(),
                "areas": self.areas.json(),
                "material": self.material.json()
            }
        return None
