#Haz una función que reciba un string y dos índices. Se debe retornar el string que va entre
#las posiciones indicadas por los índices. Si las posiciones no son validas se debe avisar.

import time
import os

def fRecibir():
    os.system("cls")
    String = input("Digite algo: ")
    Indice1 = int(input("Digite un indice: "))
    Indice2 = int(input("Digite otro indice: "))

    if Indice1 > len(String) or Indice2 > len(String):
        print("Indices proporcionados, no validos!")
        print("Volviendo al programa...")
        time.sleep(3)
        return fRecibir()

    else:
        print(f"\n\tLa frase entre los indices {Indice1} y {Indice2} es: <{String[Indice1:Indice2]}>\n")
        print("Volviendo al programa...")
        time.sleep(5)
        return fRecibir()

fRecibir()
