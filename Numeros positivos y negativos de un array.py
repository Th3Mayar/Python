#9- Realizar un programa que, tras asignar los números, -3, 6, 7, -8, 11, 16 y -3 a un
#array calcule independientemente la suma de los elementos positivos y negativos
#de manera separada.

num = 0
vSuma1 = 0
vSuma2 = 0

sAsignar = [-3, 6, 7, -8, 11, 16, -3]
vPositivo = list(filter(lambda x: x >= 0, sAsignar))
vNegativo = list(filter(lambda x: x < 0, sAsignar))

for item in vPositivo:
    vSuma1 = vSuma1 + item

for item in vNegativo:
    vSuma2 = vSuma2 + item

print(f"Los positivos son: {vPositivo}")
print(f"La suma de los positivos es: {vSuma1}")
print(f"Los negativos son: {vNegativo}")
print(f"La suma de los positivos es: {vSuma2}")