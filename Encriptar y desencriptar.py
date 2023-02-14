#Realizar un algoritmo que le muestre al usuario la opción de encriptar
#o desencriptar una frase ingresada previamente por el teclado, dicho programa
#debe de cumplir las siguientes reglas:

import os
import time
import str

vOp = 0

def fCondicion():    
    Count1 = sFrase.count('a')
    Count2 = sFrase.count('e')
    Count3 = sFrase.count('i')
    Count4 = sFrase.count('o')
    Count5 = sFrase.count('u')

    Count6 = sFrase.count('A')
    Count7 = sFrase.count('E')
    Count8 = sFrase.count('I')
    Count9 = sFrase.count('O')
    Count10 = sFrase.count('O')

    if (Count1 >= 1 or Count2 >= 1 or Count3 >= 1 or Count4 >= 1 or Count5 >= 1 or Count6 >= 1 or Count7 >= 1 or Count8 >= 1 or Count9 >= 1 or Count10 >= 1):
        print("Es admitido, al menos introdujo una vocal en la frase")
        os.system("\npause")
    
    elif (Count1 < 1 or Count2 < 1 or Count3 < 1 or Count4 < 1 or Count5 < 1 or Count6 < 1 or Count7 < 1 or Count8 < 1 or Count9 < 1 or Count10 < 1):
        print("Lo siento, digite de nuevo una frase")
        os.system("\npause")

def fEncriptar(sFrase):
    sCambio = {'a' : '15', 'e' : '14', 'i' : '13', 'o' : '12', 'u' : '11'}
    sCambio = {'A' : '15', 'E' : '14', 'I' : '13', 'O' : '12', 'U' : '11'}

    Cambio = sFrase.maketrans(sCambio)
    print(sFrase.translate(Cambio))

def fDesencriptar(sFrase):
    sCambio = {15 : 'a', 14 : 'e', 13 : 'i', 12 : 'o', 11 : 'u'}
    sCambio = {15 : 'A', 14 : 'E', 13 : 'I', 12 : 'O', 11 : 'U'}

    Cambio = sFrase.maketrans(sCambio)

    print(sFrase.translate(Cambio))

while True:

    os.system("cls")
    print("""
            
            1 - Ingresar Frase
            2 - Encriptar Frase
            3 - Desencriptar Frase
            4 - Salir del Sistema

        """)

    vOp = int(input("Digite una opcion: "))

    if (vOp == 1):
        sFrase = input("¿Qué frase quieres encriptar? -> ")
        CountFrase = len(sFrase)
        if (CountFrase > 4):
            print("Puede seguir con el programa...")
            fCondicion()
        else:
            sFrase = ' '
            print("Lo siento, la frase tiene de 4 caracteres abajo.")
            os.system("\npause")

    elif (vOp == 2):
        if (sFrase == ' '):
            print("No hay ninguna frase para encriptar")
            os.system("\npause")
        else:
            print("Encriptando password...")
            time.sleep(2)
            Encriptar = fEncriptar(sFrase)
            print("Frase encriptada")
            os.system("\npause")
        

    elif (vOp == 3):
        if (sFrase == ' '):
            print("No hay ninguna frase para desencriptar")
            os.system("\npause")
        else:
            print("Desencriptando frase...")
            time.sleep(5)
            fDesencriptar(sFrase)
            print("Frase desencriptada")
            os.system("\npause")

    elif (vOp == 4):
        break

    else:
        print("Opcion no valida, intente de nuevo")