#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información
#sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
#que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el
#contenido del diccionario.

import os

while True:
    os.system("cls")
    Diccionario = {}
    Nombre = input("Nombre: ")
    Diccionario['Nombre'] = Nombre #Guardar valor en el diccionario
    print(Diccionario) #Mostrar contenido
    Edad = input("Edad: ")
    Diccionario['Edad'] = Edad #Guardar valor en el diccionario
    print(Diccionario) #Mostrar contenido
    Sexo = input("Sexo -> Masculino/Femenino: ")
    Diccionario['Sexo'] = Sexo #Guardar valor en el diccionario
    print(Diccionario) #Mostrar contenido
    Telefono = input("Telefono: ")
    Diccionario['Telefono'] = Telefono #Guardar valor en el diccionario
    print(Diccionario) #Mostrar contenido
    Direccion = input("Direccion: ")
    Diccionario['Direccion'] = Direccion #Guardar valor en el diccionario
    print(Diccionario) #Mostrar contenido
    Correo = input("Correo Electronido: ")
    Diccionario['Correo Electronido'] = Correo #Guardar valor en el diccionario
    print(Diccionario) #Mostrar contenido

    print(Diccionario)
    os.system("pause")
