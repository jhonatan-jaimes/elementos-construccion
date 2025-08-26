class Medidas2D:
    def __init__(self, largo: float = 0.0, ancho: float = 0.0):
        self.largo = largo
        self.ancho = ancho


class Medidas3D(Medidas2D):
    def __init__(self, largo: float = 0.0, ancho: float = 0.0, alto: float = 0.0):
        super().__init__(largo, ancho)
        self.alto = alto


medidas_2d = Medidas2D()
medidas_3d = Medidas3D()
