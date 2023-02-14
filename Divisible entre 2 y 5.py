#Realice un programa que indique si un número es divisible entre dos y cinco (a la vez)

vNum = int(input("Digite un numero: "))

if (vNum %2 == 0 and vNum %5 == 0):
    print("El numero es divisible entre 2 y 5")

else:
    print("El numero no es divisible entre 2 ni 5")