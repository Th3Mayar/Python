#Escribir un programa que indique si una persona tiene sobrepeso (observar la
#imagen de ejemplo como parámetros a utilizar) Los datos deben ser positivos.

print("""

ELIJA SU ALTURA en KG

    1.45 - 1.47 - 1.49 - 1.51 - 1.53
    1.55 - 1.57 - 1.59 - 1.61 - 1.63
    1.65 - 1.67 - 1.69 - 1.71 - 1.73
    1.75 - 1.77 - 1.79 - 1.81 - 1.83
    1.85 - 1.87 - 1.89 - 1.91

""")

vAltura = float(input("Cuanto mide usted? "))
vPeso = float(input("Cuanto pesa usted en Kg, no es necesario que ponga Kg: "))

if (vAltura == 1.45 and vPeso <= 52.5 or vAltura == 1.47 and vPeso <= 54.0 or vAltura == 1.49 and vPeso <= 55.5 or vAltura == 1.51 and vPeso <= 57.0 or vAltura == 1.53 and vPeso <= 58.5 or vAltura == 1.55 and vPeso <= 60.0 or vAltura == 1.57 and vPeso <= 61.6 or vAltura == 1.59 and vPeso <= 63.2 or vAltura == 1.61 and vPeso <= 64.8 or vAltura == 1.63 and vPeso <= 66.4 or vAltura == 1.65 and vPeso <= 68.0 or vAltura == 1.67 and vPeso <= 69.7 or vAltura == 1.69 and vPeso <= 71.4 or vAltura == 1.73 and vPeso <= 74.8 or vAltura == 1.75 and vPeso <= 78.3 or vAltura == 1.77 and vPeso <= 80.1 or vAltura == 1.79 and vPeso <= 80.1 or vAltura == 1.81 and vPeso <= 83.7 or vAltura == 1.83 and vPeso <= 85.5 or vAltura == 1.85 and vPeso <= 87.1 or vAltura == 1.87 and vPeso <= 89.3 or vAltura == 1.91 and vPeso <= 91.2):
    print("\nUsted no tiene sobrepeso\n")

else:
    print("\nUsted tiene sobrepeso\n")