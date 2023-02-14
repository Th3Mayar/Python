#Realizar un programa que indique cuál es el mayor de cuatro números enteros ingresados por el teclado.

vNum1 = int(input("Digite el primer numero: "))
vNum2 = int(input("Digite el segundo numero: "))
vNum3 = int(input("Digite el tercer numero: "))
vNum4 = int(input("Digite el cuarto numero: "))

if (vNum1 > vNum2) and (vNum1 > vNum3) and (vNum1 > vNum4):
    print(f'El mayor es el primero: {vNum1}')

elif (vNum2 > vNum1) and (vNum2 > vNum3) and (vNum2 > vNum4):
    print(f'El mayor es el segundo: {vNum2}')

elif (vNum3 > vNum1) and (vNum3 > vNum2) and (vNum3 > vNum4):
    print(f'El mayor es el tercero: {vNum3}')

elif (vNum1 == vNum2 or vNum1 == vNum3 or vNum2 == vNum1 or vNum2 == vNum3 or vNum3 == vNum1 or vNum3 == vNum2 or vNum4 == vNum1 or vNum4 == vNum3 or vNum4 == vNum2):
    print("Todos o algunos de los valores son iguales")

else:
    print(f'El mayor es el cuarto: {vNum4}')
