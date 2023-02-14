#6- Realizar una función que reciba datos tipo string e imprima su valor en la tabla ascii
#6- Create a function that receives string data and prints its value in the ascii table

import os
import time

def fRecibir():
    os.system("cls")
    Ascii = input("\n\tDigite un dato de la tabla ascii en texto: ")
    for item in Ascii:
        print(f"\n\tEn codico ascii el {Ascii} es: ( Alt + ",ord(item),")\n")
        os.system("pause")
        return fRecibir()

fRecibir()