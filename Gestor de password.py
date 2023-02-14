# SPANISH (Realizar un programa que permita generar contraseñas seguras.)

# ENGLISH (Make a program that allows you to generate secure passwords.)

from pickle import TRUE
from docx2pdf import convert
from random import *
from ast import main
import string
import random
import time
import sys
import os

mayus = False
minus = False
num = False
longitud = 8

def fIngresar(Introducir):
    import os
    while True:
        try:
            vTexto = int(input(Introducir))
        except ValueError:
            (print("\nPor favor, ingrese un numero entero...\n"))
            os.system("pause")
        else:
            break
    return vTexto

def fGenerar_Pass(longitud = 8, Mayusculas = False, Minusculas = False, Numeros = False):
    caracteres = []
    if(Mayusculas):
        caracteres += string.ascii_uppercase

    if(Minusculas):
        caracteres += string.ascii_lowercase

    if(Numeros):
        caracteres += string.digits

    while True:
        max = True
        min = True
        num = True
        sim = True
        contraseña = "".join(random.choice(caracteres) for i in range(longitud))
        if(Mayusculas):
            max = False
            for i in contraseña:
                if (i.isupper()):
                    max = True
        if(Minusculas):
            min = False
            for i in contraseña:
                if (i.islower()):
                    min = True
        if(Numeros):
            num = False
            for i in contraseña:
                if (i.isdigit()):
                    num = True
        if(max and min and num and sim):
            break

    return contraseña

def fFormato():
    os.system("cls")
    os.system("color 0F")
    print("""
        ┌─────────────────────────────────────────────────────────┐
        │               Menu Gestor de contraseñas                │
        │_________________________________________________________│
        │                                                         │
        │    1- .txt                                              │
        │    2- .docx                                             │
        │    3- .xlsx                                             │
        │    4- Otro                                              │
        │    5- Volver                                            │
        │                                                         │
        └─────────────────────────────────────────────────────────┘ 
    """)
    TipoArchivo = input("\n\tElija un formato de archivo para guardar la pass: ")

    if (TipoArchivo == '1'):
        archivo = open("Semana 08\Contraseña.txt", "a")
        archivo.write(fAutomatico + '\n')
        archivo.close()
        print("\n\tContraseña guardada en el archivo\n")

    elif (TipoArchivo == '2'):
        archivo = open("Semana 08\Contraseña.docx", "a")
        archivo.write(fAutomatico + '\n')
        archivo.close()
        print("\n\tContraseña guardada en el archivo\n")

    elif (TipoArchivo == '3'):
        archivo = open("Semana 08\Contraseña.xlsx", "a")
        archivo.write(fAutomatico + '\n')
        archivo.close()
        print("\n\tContraseña guardada en el archivo\n")
    
    
    elif (TipoArchivo == '4'):
        TipoArchivoIngresar = input("\n\tDigame usted el tipo de formato de archivo desea: ")
        archivo = open("Semana 08\Contraseña"+TipoArchivoIngresar, "a")
        archivo.write(fAutomatico + '\n')
        archivo.close()
        print("\n\tContraseña guardada en el archivo\n")
    
    elif (TipoArchivo == 5):
        return main()

while True:
    Encriptar = ''
    os.system("cls")
    os.system("color F0")
    print("""
        ┌─────────────────────────────────────────────────────────┐
        │               Menu Gestor de contraseñas                │
        │_________________________________________________________│
        │                                                         │
        │    1- Ingresar Longitud (Default 8)                     │
        │    2- Generar pass automaticamente                      │
        │    3- Generar pass con opciones                         │
        │    4- Incluir Mayúsculas                                │
        │    5- Incluir Minúsculas                                │
        │    6- Incluir números                                   │
        │    7- Desactivar todas las opciones                     │
        │    8- Salir                                             │
        │                                                         │
        └─────────────────────────────────────────────────────────┘ 
    
    """)
    Op = fIngresar("\tIngrese una opcion: ")

    if(Op == 1):
        while True:
            longitud = fIngresar("\tIntroduce la longitud de la contraseña: ")
            if longitud >= 8:
                break
            else:
                print("\nLa longitud debe de ser mayor o igual a 8")

    elif (Op == 2):
        def fAutomatico(longitud):
            minusculas = string.ascii_lowercase
            mayusculas = string.ascii_uppercase
            numeros = string.digits
            secuencia = minusculas + mayusculas + numeros
            fAutomatico = sample(secuencia, longitud)
            resultado = "".join(fAutomatico)
            return resultado
        fAutomatico = fAutomatico(longitud)
        for item in range(len(fAutomatico)):
            Encriptar = Encriptar + '*'
        print("\n\tLa contraseña generada es: ", Encriptar, "\n")
        Guardar = input("\n\t¿Deseas guardarla en un archivo? (S/N): ").upper()
        if Guardar == "S":
            fFormato()
        else:
            print("\n\tContraseña no guardada\n")

    elif(Op == 3):
        if(mayus == False and minus == False and num == False):
            print("\tDebe Activar al menos una opcion...")

        else:
            contraseña = fGenerar_Pass(longitud, mayus, minus, num)
            for item in range(len(contraseña)):
                Encriptar = Encriptar + '*'
            print("\n\tLa contraseña generada es: ", Encriptar)
            Guardar = input("\n\t¿Deseas guardarla en un archivo? (S/N): ").upper()
            if Guardar == "S":
                fFormato()
            else:
                print("\n\tContraseña no guardada\n")

    elif(Op == 4):
        if(mayus == False):
            mayus = True
            print("\n\tSe ha activado la opción de mayúsculas.\n")
        else:
            print("\n\tLa opción de mayúsculas ya está activada.\n")

    elif(Op == 5):
        if(minus == False):
            minus = True
            print("\n\tSe ha activado la opción de minúsculas.\n")
        else:
            print("\n\tLa opción de minúsculas ya está activada.\n")

    elif(Op == 6):
        if(num == False):
            num = True
            print("\tSe ha activado la opción de números.\n")
        else:
            print("\tLa opción de números ya está activada.\n")

    elif(Op == 7):
        if(mayus == False and minus == False and num == False):
            print("\tNo se ha activado ninguna opción.\n")
        else:
            print("\tSe han desactivado todas las opciones.\n")
            mayus = False
            minus = False
            num = False

    elif(Op == 8):
        exit()
    
    print("\n")
    os.system("pause")