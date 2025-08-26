from src.medidas import Medidas3D, Medidas2D
from src.implement import implement as imp


def run():
    nombre = input("Ingrese el nombre del elemento: \n")
    largo = float(input("Ingrese el largo del elemento: \n"))
    ancho = float(input("Ingrese el ancho del elemento: \n"))
    alto = float(input("Ingrese el ancho del elemento: \n"))
    cantidad = int(input("Ingrese la cantidad de elementos: \n"))
    material = input("Material del elemento: \n")
    dosificacion = input("Dosificacion del material: \n")
    med_3d = Medidas3D(largo, ancho, alto)
    element = imp.elemento(nombre, med_3d, cantidad, dosificacion, material)

    print(element.json())


if __name__ == '__main__':
    run()
