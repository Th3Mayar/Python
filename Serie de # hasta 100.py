#Escribir un programa que sume la serie 2, 4, 6, hasta el 100 y despliegue su resultado.

Suma = 0

while True:

    for item in range(2,101,2):
        Suma = Suma + item
        print(f"->{item}")
    
    break

print(f"\nLa suma es: {Suma}\n\n")