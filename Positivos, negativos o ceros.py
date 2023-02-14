#Escribir un programa que indica cuantos valores positivos, negativos o 0 fueron
#ingresados por el teclado de un conjunto de 10 datos (utilizar estructura se control for).

Cont = 0
Positivo = 0
Negativo = 0
Cero = 0

while Cont != 10:
    
    for item in range(10):
        vNum1 = int(input("Digite el numero: "))
        Cont = Cont + 1

        if (Cont == 0):

            Positivo = vNum1
            Negativo = vNum1
            Cero = vNum1

        elif (vNum1 < 0):
            Negativo = Negativo + 1
            

        elif (vNum1 > 0):
            Positivo = Positivo + 1
        
        elif (vNum1 == 0):
            Cero = Cero + 1

else:
    print("\n\n------------------------")
    print(f"| Positivos: {Positivo}")
    print(f"| Negativos: {Negativo}")
    print(f"| Ceros: {Cero}")
    print("------------------------\n\n")