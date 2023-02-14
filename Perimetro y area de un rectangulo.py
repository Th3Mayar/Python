#Escribir un programa que calcule el perímetro y área de un rectángulo

fBase = float(input("Digite la base del rectangulo: "))
fAltura = float(input("Digite la altura: "))

vPerimetro = 2 * (fBase + fAltura) 
vArea = fBase * fAltura

print(f'El perimetro del rectangulo es: {vPerimetro}')
print(f'El area del rectangulo es: {vArea}')

