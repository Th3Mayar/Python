#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$',
#'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso
#si la divisa no está en el diccionario.

import os

Diccionario = {

    'Euro': '€',
    'Dollar': '$',
    'Yen': '¥',
    '€': 'Euro',
    '$': 'Dollar',
    '¥': 'Yen'

}

while True:
    os.system("cls")
    print("""
        ┌─────────────────────────────────────────────────────────┐
        │        Quieres ver si la divisa esta disponible?        │
        │_________________________________________________________│
        │                                                         │
        │    1- Digite la divisa                                  │
        │    2- Salir                                             │
        │                                                         │
        └─────────────────────────────────────────────────────────┘ 
    """)
    Op = input("Digite una opcion: ")
            
    if Op == '1':
        sDivisa = input("Digite una divisa: ")

        if sDivisa in Diccionario:
            print(f"La divisa {sDivisa} se encuentra en el diccionario y es {Diccionario[sDivisa]}")

        elif Op == '2':
            exit()

        else:
            print(f"La divisa no se encuentra en el diccionario")
    else:
            print("Lo siento, intentelo de nuevo")

    os.system("pause")

