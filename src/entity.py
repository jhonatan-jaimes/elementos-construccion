class Material:
    def __init__(self, tipo: str = "", cemento: float = 0.0, arena: float = 0.0, grava: float = 0.0,
                 agua: float = 0.0):
        self.tipo = tipo
        self.cemento = cemento
        self.arena = arena
        self.agua = agua
        self.grava = grava

    def json(self):
        return {
            "tipo": self.tipo,
            "cemento": self.cemento,
            "arena": self.arena,
            "grava": self.grava,
            "agua": self.agua
        }


class Areas:
    def __init__(self):
        self.area_one = 0.0
        self.area_all = 0.0

    def json(self):
        return {
            "areaUnidad": self.area_one,
            "areaTotal": self.area_all
        }


class Medidas:
    def __init__(self, tipo: str = "", largo: float = 0.0, ancho: float = 0.0, alto: float = 0.0):
        self.tipo = tipo
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

    def json(self):
        return {
            "tipo": self.tipo,
            "largo": self.largo,
            "ancho": self.ancho,
            "alto": self.alto
        }


class Elemento:
    def __init__(self, nombre: str = "", cantidad: int = 0, medidas: Medidas = None,
                 areas: Areas = None, material: Material = None):
        self.nombre = nombre
        self.cantidad = cantidad
        self.medidas = medidas
        self.areas = areas
        self.material = material

    def json(self):
        return {
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "medidas": self.medidas.json(),
            "areas": self.areas.json(),
            "material": self.material.json()
        }
