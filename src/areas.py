from decimal import Decimal as dec
from src.medidas import Medidas2D, Medidas3D


class Areas:
    def __init__(self):
        self.area_one = 0.0
        self.area_all = 0.0

    def calcular_all(self, cantidad: int):
        self.area_all = self.area_one * cantidad

