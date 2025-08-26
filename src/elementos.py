from src.areas import Areas


class Elemento:
    def __init__(self, nombre: str = "", cantidad: int = 0, medidas: object = None,
                 areas: Areas = None, material: object = None):
        self.nombre = nombre
        self.cantidad = cantidad
        self.medidas = medidas
        self.areas = areas
        self.material = material

    def json(self):
        pass

