#Escribir un programa que calcule al perímetro y área de un círculo dado su radio

fRadio = float(input("Ingrese el radio: "))

fArea = 3.141592 * (fRadio ** 2)
fPerimetro = 3.141592 * (fRadio * 2)

print(f'El area del circulo es: {fArea}')
print(f'El perimetro del circulo es: {fPerimetro}')
