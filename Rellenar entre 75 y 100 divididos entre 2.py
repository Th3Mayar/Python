#3- Realizar un programa que rellene una lista con los números comprendidos entre
#75 y 100 divididos por 2. 

Rellenar = []

for item in range(75, 101, 1):
    Rellenar = Rellenar + [item/2]

print(Rellenar)