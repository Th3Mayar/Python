#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
#pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de
#ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje
#informando de ello.

import os

Diccionario = {

    'Platano' : 1.35,
    'Manzana' : 0.80,
    'Pera' : 0.85,
    'Naranja' : 0.70

}

def fMain():
    while True:
        os.system("cls")
        Fruta = input("Que fruta desea comprar?, frutas disponibles (0), salir (1): ")
        Kilos = int(input("Digite la cantidad de kilos que desea?: "))

        if Fruta in Diccionario:
            print(f"El precio de {Fruta} x unidad es de {Fruta[Diccionario]} es de ${Diccionario[Fruta]*Kilos}")

        elif Fruta == '0':
            print("""

                ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                ▀ LAS FRUTAS DISPONIBLES SON: ▀
                ▀                             ▀
                ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                ▀   Platano                   ▀
                ▀   Manzana                   ▀
                ▀   Pera                      ▀
                ▀   Naranja                   ▀
                ▀                             ▀
                ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            """)
            
        elif Fruta == '1':
            print("Gracias por participar - Created by @Th3Mayar")
            exit()

        elif Fruta not in Diccionario:
            print("La fruta no se encuentra dentro del diccionario")
            fMain()

        else:
            print("Opcion no valida")
        
        os.system("pause")

fMain()