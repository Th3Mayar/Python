#6- Realizar un programa que rellene una lista con los 40 primeros números pares y
#calcule su suma y promedio.

Rellenar = []
vSuma = 0
vPromedio = 0
Cont = 0

for item in range(2, 41, 2):
    Cont = Cont + 1
    Rellenar = Rellenar + [item]
    vSuma = vSuma + item

print(Rellenar) 
print(f'La suma es: {vSuma}')
print(f'El promedio es: {vSuma / Cont}')