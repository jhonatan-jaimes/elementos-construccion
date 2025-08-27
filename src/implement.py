from .service import Service
from .entity import Areas, Elemento, Material, Medidas
from decimal import Decimal as dec


class Implement(Service):
    def __init__(self):
        self.dosificacion_concreto = {
            ("1:2:2", "280", "4000", "27"):
                {"cemento": "420", "arena": "0.67", "grava": "0.67", "agua": "190"},
            ("1:2:2.5", "240", "3555", "24"):
                {"cemento": "380", "arena": "0.60", "grava": "0.76", "agua": "180"},
            ("1:2:3", "226", "3224", "22"):
                {"cemento": "350", "arena": "0.55", "grava": "0.84", "agua": "170"},
            ("1:2:3.5", "210", "3000", "20"):
                {"cemento": "320", "arena": "0.52", "grava": "0.90", "agua": "170"},
            ("1:2:4", "200", "2850", "19"):
                {"cemento": "300", "arena": "0.48", "grava": "0.95", "agua": "158"},
            ("1:2:4.5", "189", "2700", "18"):
                {"cemento": "280", "arena": "0.55", "grava": "0.89", "agua": "158"},
            ("1:3:3", "168", "2400", "16"):
                {"cemento": "300", "arena": "0.72", "grava": "0.72", "agua": "158"},
            ("1:3:4", "159", "2275", "15"):
                {"cemento": "260", "arena": "0.63", "grava": "0.83", "agua": "163"},
            ("1:3:5", "140", "2000", "14"):
                {"cemento": "230", "arena": "0.55", "grava": "0.92", "agua": "148"},
            ("1:3:6", "119", "1700", "12"):
                {"cemento": "210", "arena": "0.50", "grava": "1.00", "agua": "143"},
            ("1:4:7", "109", "1560", "11"):
                {"cemento": "175", "arena": "0.55", "grava": "0.98", "agua": "133"},
            ("1:4:8", "99", "1420", "10"):
                {"cemento": "160", "arena": "0.55", "grava": "1.03", "agua": "125"}
        }

        self.dosificacion_mortero = {
            ("1:2", "310", "4400", "30"):
                {"cemento": "525", "arena": "0.97", "agua": "230"},
            ("1:3", "280", "3980", "27"):
                {"cemento": "450", "arena": "1.10", "agua": "210"},
            ("1:4", "240", "3400", "23"):
                {"cemento": "375", "arena": "1.16", "agua": "200"},
            ("1:5", "200", "2850", "19"):
                {"cemento": "300", "arena": "1.18", "agua": "180"},
            ("1:6", "160", "2275", "16"):
                {"cemento": "275", "arena": "1.20", "agua": "180"},
        }

    def area(self, medidas: Medidas, cantidad: int):
        areas = Areas()
        if medidas.tipo.lower() == "3d":
            areas.area_one = round(float(dec(medidas.largo * medidas.ancho * medidas.alto)), 2)
            areas.area_all = round(float(dec(areas.area_one * cantidad)), 2)

            return areas

        elif medidas.tipo.lower() == "2d":
            areas.area_one = round(float(dec(medidas.largo * medidas.ancho)), 2)
            areas.area_all = round(float(dec(areas.area_one * cantidad)), 2)

            return areas

        else:

            return None

    def material(self, area: Areas, dosificacion: str, material_tipo: str):
        material = Material()

        if material_tipo.lower() == "concreto":

            objeto_dosificacion = None

            for clave in self.dosificacion_concreto:
                if dosificacion in clave:
                    objeto_dosificacion = self.dosificacion_concreto[clave]
                    break

            material.tipo = material_tipo.lower()
            material.cemento = float(round(dec(area.area_all) * dec(objeto_dosificacion["cemento"]), 2))
            material.arena = float(round(dec(area.area_all) * dec(objeto_dosificacion["arena"]), 2))
            material.grava = float(round(dec(area.area_all) * dec(objeto_dosificacion["grava"]), 2))
            material.agua = float(round(dec(area.area_all) * dec(objeto_dosificacion["agua"]), 2))

            return material

        elif material_tipo.lower() == "mortero":

            objeto_dosificacion = None

            for i in self.dosificacion_mortero:
                if dosificacion in i:
                    objeto_dosificacion = self.dosificacion_mortero[i]
                    break

            area_corregida = float(round(dec(area.area_all * 0.01), 2))

            material.tipo = material_tipo.lower()
            material.cemento = float(round(dec(area_corregida) * dec(objeto_dosificacion["cemento"]), 2))
            material.arena = float(round(dec(area_corregida) * dec(objeto_dosificacion["arena"]), 2))
            material.grava = 0.0
            material.agua = float(round(dec(area_corregida) * dec(objeto_dosificacion["agua"]), 2))

            return material

        else:

            return None

    def elemento(self, nombre: str, medidas: Medidas, cantidad: int, dosificacion: str, material_tipo: str):
        area = self.area(medidas, cantidad)
        material = self.material(area, dosificacion, material_tipo)
        elem = Elemento(nombre, cantidad, medidas, area, material)

        return elem


implement = Implement()
