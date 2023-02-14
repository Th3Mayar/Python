#Realice un programa que indique si la suma de dos valores es positiva, negativa o cero.

vValor1 = int(input("Ingrese el primer valor: "))
vValor2 = int(input("Ingrese el segundo valor: "))

oSuma = vValor1 + vValor2

if (oSuma < 0):
    print(f"La suma es Negativa -> {oSuma}")

elif (oSuma == 0):
    print("La suma es cero")

else:
    print(f"La suma es positiva -> {oSuma}")