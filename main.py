from src.areas import Areas
from src.medidas import Medidas2D, Medidas3D


def run():
    medidas = Medidas3D(23.4, 25.6, .3)
    area = Areas()
    area.calcular_area(medidas, 20)
    print(area.area_one, area.area_all)


if __name__ == '__main__':
    run()
