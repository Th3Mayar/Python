#Escribir un programa que lea por teclado 10 números y muestre en pantalla
#el más grande, el más pequeño y la media de N los números ingresados

Cont = 0
vMayor = 0
vMenor = 0
vMedia = 0

while Cont != 10:
    
    for item in range(10):
        vNum1 = int(input("Digite el numero: "))
        Cont = Cont + 1

        if (Cont == 1):

            vMenor = vNum1
            vMayor = vNum1

        elif (vNum1 < vMenor):
            vMenor = vNum1

        elif (vNum1 > vMayor):
            vMayor = vNum1
        
        vMedia = vMedia + vNum1

else:
    print("\n\n------------------------")
    print(f"| El mas grande es: {vMayor}")
    print(f"| El mas pequeño es: {vMenor}")
    print(f"| La media es: {round(vMedia/Cont)}")
    print("------------------------\n\n")