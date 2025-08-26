from decimal import Decimal as dec


class Medidas2D:
    def __init__(self, largo: float = 0.0, ancho: float = 0.0):
        self.largo = largo
        self.ancho = ancho

    def calcular(self):
        return float(round(dec(self.largo * self.ancho), 2))


class Medidas3D(Medidas2D):
    def __init__(self, largo: float = 0.0, ancho: float = 0.0, alto: float = 0.0):
        super().__init__(largo, ancho)
        self.alto = alto

    def calcular(self):
        return float(round(dec(super().calcular() * self.alto), 2))
