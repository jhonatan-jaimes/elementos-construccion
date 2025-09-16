from src import Medidas
from src import implement as imp
from src.data_base import ddbb

med = Medidas()


def run():
    seguir = True
    imprimir = False
    while seguir:
        tipo_medidas = input("Que tipo es: [ 3D/2D ] ")
        if tipo_medidas.lower() == "2d":
            nombre = input("Ingrese el nombre del elemento: ")
            largo = float(input("Ingrese el largo del elemento: "))
            ancho = float(input("Ingrese el ancho del elemento: "))
            cantidad = int(input("Ingrese la cantidad de elementos: "))
            material = input("Material del elemento: ")
            dosificacion = input("Dosificacion del material: ")
            med_3d = Medidas(tipo_medidas, largo, ancho)
            element = imp.elemento(nombre, med_3d, cantidad, dosificacion, material)
            imp.save_ele(element)
        elif tipo_medidas.lower() == "3d":
            nombre = input("Ingrese el nombre del elemento: ")
            largo = float(input("Ingrese el largo del elemento: "))
            ancho = float(input("Ingrese el ancho del elemento: "))
            alto = float(input("Ingrese el alto del elemento: "))
            cantidad = int(input("Ingrese la cantidad de elementos: "))
            material = input("Material del elemento: ")
            dosificacion = input("Dosificacion del material: ")
            med_3d = Medidas(tipo_medidas, largo, ancho, alto)
            element = imp.elemento(nombre, med_3d, cantidad, dosificacion, material)
            imp.save_ele(element)
        select = input("Desea ver elementos: [ y/n ] ")
        if select.lower() == "y":
            for e in ddbb.data_base:
                print(e.json())

        conti = input("Desea continuar? [ y/n ] ")
        if conti.lower() == "n":
            seguir = False


if __name__ == '__main__':
    run()
