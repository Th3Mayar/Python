import math

#Escribir un programa que calcule la hipotenusa de un triángulo rectángulo

vCatetoHorizontal = float(input("Digite el cateto horizontal: "))
vCatetoVertical = float(input("Digite el cateto vertical: "))

fHipotenusa = (vCatetoHorizontal ** 2) + (vCatetoVertical ** 2)

print(f'La hipotenusa o lado C del triángulo rectangulo es de: {math.sqrt(fHipotenusa)} cm')