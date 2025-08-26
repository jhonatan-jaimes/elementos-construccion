from src.entity import Medidas
from src.ddbb import ddbb
from src.implement import implement as imp

med = Medidas()


def run():
    seguir = True
    imprimir = False
    while seguir:
        nombre = input("Ingrese el nombre del elemento: ")
        tipo_medidas = input("Que tipo es: [ 3D/2D ] ")
        largo = float(input("Ingrese el largo del elemento: "))
        ancho = float(input("Ingrese el ancho del elemento: "))
        alto = float(input("Ingrese el alto del elemento: "))
        cantidad = int(input("Ingrese la cantidad de elementos: "))
        material = input("Material del elemento: ")
        dosificacion = input("Dosificacion del material: ")
        med_3d = Medidas(tipo_medidas, largo, ancho, alto)
        element = imp.elemento(nombre, med_3d, cantidad, dosificacion, material)
        ddbb.data_base.append(element)

        select = input("Desea ver elementos: [ y/n ] ")
        if select.lower() == "y":
            for e in ddbb.data_base:
                print(e.json())


if __name__ == '__main__':
    run()
