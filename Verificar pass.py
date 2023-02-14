#Escribir un programa que verifica si un dato ingresado por teclado corresponde a
#la contraseña 123456 y no deje de preguntar por la contraseña hasta que la misma
#sea la correcta.

while True:

    for item in range(1):
        vPass = input("Digite la pass: ")
    
    if (vPass != '123456'):
        print("Intentelo de nuevo, buena suerte")
    
    else:
        print("\n\nBienvenido al sistema <3\n\n")
        break