#4- Realizar un programa que rellene una lista con 10 números enteros consecutivos
#y haga una copia de ese array en otro.

Rellenar = []
Copia = []

for item in range(10):

    vNum = input("Digite 10 numeros consecutivos: ")
    Rellenar = Rellenar + [vNum]

Copia = Copia + [Rellenar]

print(Copia)