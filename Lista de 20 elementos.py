#5- Realizar un programa que rellene una lista de 20 elementos con los números
#comprendidos entre 20 y 39 y copie en otro array esos números multiplicados por
#0.18.

Rellenar = []
Copia = []

for item in range(20, 40, 1):
    Rellenar = Rellenar + [item]
    Copia = Copia + [item * 0.18]
    
print(Copia)