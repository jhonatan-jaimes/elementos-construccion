from src import Medidas2D, Medidas3D
from service import Service
from areas import areas
from decimal import Decimal as dec


class Implement(Service):
    def areas(self, medidas: object, cantidad: int):
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

    def concreto(self):
        pass

    def mortero(self):
        pass

    def elemento(self):
        pass
