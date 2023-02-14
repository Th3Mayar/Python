#10-Realizar un programa que tras asignar 10 valores enteros en un array, determine
#las posiciones del array en las que se encuentran el máximo y el mínimo valor.

Array = []
Max = 0
Min = 0

for item in range(0, 10, 1):
    vNum = input(f"Digite el numero en la Posicion {item}: ")
    Array = Array + [vNum]

Max = max([int(num) for num in Array])
Min = min([int(num) for num in Array])

print(f"El valor menor es: {Min} y se encuentra en la posicion: {Array.index(str(Min))}")
print(f"El valor mayor es: {Max} y se encuentra en la posicion: {Array.index(str(Max))}")