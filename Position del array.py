#8- Realizar un programa que, tras ingresar seis números enteros en un array,
#determine la posición del array en la que se encuentra el máximo valor

Array = []
Max = 0

for item in range(0, 6, 1):
    vNum = input(f"Digite el numero en la Posicion {item}: ")
    Array = Array + [vNum]

Max = max([int(num) for num in Array])

print(f"El valor mayor es: {Max} y se encuentra en la posicion: {Array.index(str(Max))}")