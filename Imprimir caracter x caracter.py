#Haz un programa que reciba un string y lo imprima carácter por carácter.
#Make a program that receives a string and prints it character by character.

import time
import os
vTexto = input("Digite un texto cualquiera: ")
Cont = 0

for item in range(len(vTexto)):
    os.system("cls")
    Cont = Cont + 1
    print(vTexto[0:0+Cont])
    time.sleep(1)