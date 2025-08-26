from src.medidas import Medidas3D
from src.implement import Implement

imp = Implement()


def run():
    med_3d = Medidas3D(20.2, 10.1, .3)
    element = imp.elemento("Columna", med_3d, 2, "123", "concreto")

    print(element.areas.area_all)


if __name__ == '__main__':
    run()
