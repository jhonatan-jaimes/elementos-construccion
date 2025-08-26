class Medidas2D:
    def __init__(self, largo: float = 0.0, ancho: float = 0.0):
        self.largo = largo
        self.ancho = ancho

    def json(self):
        return {
            "largo": self.largo,
            "ancho": self.ancho
        }


class Medidas3D(Medidas2D):
    def __init__(self, largo: float = 0.0, ancho: float = 0.0, alto: float = 0.0):
        super().__init__(largo, ancho)
        self.alto = alto

    def json(self):
        return {
            "largo": self.largo,
            "ancho": self.ancho,
            "alto": self.alto
        }