#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo
#guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene
#<edad> años, vive en <dirección> y su número de teléfono es <teléfono>

sNombre = input("Digite su nombre: ")
vEdad = input("Digite su edad: ")
sDireccion = input("Digite su direccion: ")
vTelefono = input("Digite su telefono: ")

Diccionario = {

    'Nombre' : sNombre,
    'Edad' : vEdad,
    'sDireccion' : sDireccion,
    'Telefono' : vTelefono

}

print(f"{Diccionario['Nombre']} tiene {Diccionario['Edad']} años de edad, vive en {Diccionario['sDireccion']} y su numero de telefono es el {Diccionario['Telefono']}")