#7- Realizar un programa que solicite diez números, los almacene en un array y luego
#calcule el promedio de esos números.

Rellenar = []
vSuma = 0
vPromedio = 0
Cambio = 0

for item in range(1, 11, 1):
    vNum = int(input(f"Digite el numero {item}: "))
    vSuma = vSuma + vNum
    Rellenar = Rellenar + [str(vNum)]

print(Rellenar)
print(f'El promedio de los diez numeros es {vSuma / 10}')