#Escribir un programa que calcula el porcentaje de una cantidad

vCantidad = float(input("Digite la cantidad: "))
vPorciento = float(input("Digite el porciento en número (20)(30)(15) etc: "))

vOperacion = (vCantidad * vPorciento) / 100

print(f'El {vPorciento}% de {vCantidad} es {vOperacion}')
