from .medidas import Medidas2D, Medidas3D
from .service import Service
from .areas import Areas
from decimal import Decimal as dec
from .concreto import Concreto
from .mortero import Mortero
from .elementos import Elemento

areas = Areas()
concreto = Concreto()
mortero = Mortero()


class Implement(Service):
    def __init__(self):
        self.dosificacion_concreto = {
            ("122", "280", "4000", "27"): {"cemento": "420", "arena": "0.67", "grava": "0.67", "agua": "190"},
            ("122.5", "240", "3555", "24"): {"cemento": "380", "arena": "0.60", "grava": "0.76", "agua": "180"},
            ("123", "226", "3224", "22"): {"cemento": "350", "arena": "0.55", "grava": "0.84", "agua": "170"},
            ("123.5", "210", "3000", "20"): {"cemento": "320", "arena": "0.52", "grava": "0.90", "agua": "170"},
            ("124", "200", "2850", "19"): {"cemento": "300", "arena": "0.48", "grava": "0.95", "agua": "158"},
            ("124.5", "189", "2700", "18"): {"cemento": "280", "arena": "0.55", "grava": "0.89", "agua": "158"},
            ("133", "168", "2400", "16"): {"cemento": "300", "arena": "0.72", "grava": "0.72", "agua": "158"},
            ("134", "159", "2275", "15"): {"cemento": "260", "arena": "0.63", "grava": "0.83", "agua": "163"},
            ("135", "140", "2000", "14"): {"cemento": "230", "arena": "0.55", "grava": "0.92", "agua": "148"},
            ("136", "119", "1700", "12"): {"cemento": "210", "arena": "0.50", "grava": "1.00", "agua": "143"},
            ("147", "109", "1560", "11"): {"cemento": "175", "arena": "0.55", "grava": "0.98", "agua": "133"},
            ("148", "99", "1420", "10"): {"cemento": "160", "arena": "0.55", "grava": "1.03", "agua": "125"}
        }

        self.dosificacion_mortero = {
            ("12", "310", "4400", "30"): {"cemento": "525", "arena": "0.97", "agua": "230"},
            ("13", "280", "3980", "27"): {"cemento": "450", "arena": "1.10", "agua": "210"},
            ("14", "240", "3400", "23"): {"cemento": "375", "arena": "1.16", "agua": "200"},
            ("15", "200", "2850", "19"): {"cemento": "300", "arena": "1.18", "agua": "180"},
            ("16", "160", "2275", "16"): {"cemento": "275", "arena": "1.20", "agua": "180"},
        }

    def area(self, medidas: object, cantidad: int):
        if isinstance(medidas, Medidas3D):
            areas.area_one = round(float(dec(medidas.largo * medidas.ancho * medidas.alto)), 2)
            areas.area_all = round(float(dec(areas.area_one * cantidad)), 2)

            return areas

        elif isinstance(medidas, Medidas2D):
            areas.area_one = round(float(dec(medidas.largo * medidas.ancho)), 2)
            areas.area_all = round(float(dec(areas.area_one * cantidad)), 2)

            return areas

        else:

            return None

    def material(self, area: Areas, dosificacion_tipo: str, cantidad_tipo: str):
        if cantidad_tipo == "concreto":

            objeto_dosificacion = None

            for clave in self.dosificacion_concreto:
                if dosificacion_tipo in clave:
                    objeto_dosificacion = self.dosificacion_concreto[clave]
                    break

            concreto.cemento = float(round(dec(area.area_all) * dec(objeto_dosificacion["cemento"]), 2))
            concreto.arena = float(round(dec(area.area_all) * dec(objeto_dosificacion["arena"]), 2))
            concreto.grava = float(round(dec(area.area_all) * dec(objeto_dosificacion["grava"]), 2))
            concreto.agua = float(round(dec(area.area_all) * dec(objeto_dosificacion["agua"]), 2))

            return concreto

        elif cantidad_tipo == "mortero":

            objeto_dosificacion = None

            for i in self.dosificacion_mortero:
                if dosificacion_tipo in i:
                    objeto_dosificacion = self.dosificacion_mortero[i]
                    break

            mortero.cemento = float(round(dec(area.area_all) * dec(objeto_dosificacion["cemento"]), 2))
            mortero.arena = float(round(dec(area.area_all) * dec(objeto_dosificacion["arena"]), 2))
            mortero.agua = float(round(dec(area.area_all) * dec(objeto_dosificacion["agua"]), 2))

            return mortero

        else:

            return None

    def elemento(self, nombre: str, medidas: object, cantidad: int, dosificacion_tipo: str, cantidad_tipo: str):
        area = self.area(medidas, cantidad)
        material = self.material(area, dosificacion_tipo, cantidad_tipo)
        elem = Elemento(nombre, cantidad, medidas, areas, material)

        return elem
