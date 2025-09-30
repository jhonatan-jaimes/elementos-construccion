from .Service import Service
from entity import Medidas, Areas, Material, Elemento
from decimal import Decimal as dec
from util import tabla_mortero, tabla_concreto


class Implement(Service):
    def __init__(self):
        self.dosificacion_concreto = tabla_concreto
        self.dosificacion_mortero = tabla_mortero

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
        return Elemento(nombre, cantidad, medidas, area, material)


implement = Implement()
