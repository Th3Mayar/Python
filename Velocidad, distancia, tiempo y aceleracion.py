#Realiza un programa dado la opción elegida en un menú calcule (1) velocidad
#promedio de un vehículo; (2) la distancia recorrida; (3) Tiempo y (4) aceleración
#promedio. Se entiende que los datos introducidos están en las medidas de metros
#y segundos. 

print("""

ELIJA UNA OPCION

    1) Calcular la velocidad
    2) Calcular la distancia
    3) Calcular el tiempo
    4) Calcular la aceleracion

""")

vMenu = int(input(": "))

print("\n")

if (vMenu == 1):
    Distancia = float(input("Digite la distancia que ha recorrido el vehiculo: "))
    Tiempo = float(input("Digite el tiempo del vehiculo: "))

    oFormula = Distancia / Tiempo

    print("\n")
    print(f'V = d / t')
    print(f'V = {Distancia} m / {Tiempo} s')
    print(f'V = {oFormula} m/s')
    print("\n")

elif (vMenu == 2):
    Velocidad = float(input("Digite la velocidad  del vehiculo: "))
    Tiempo = float(input("Digite el tiempo del vehiculo: "))

    oFormula = Velocidad * Tiempo

    print("\n")
    print(f'd = v * t')
    print(f'd = {Velocidad} m/s * {Tiempo} s')
    print(f'd = {oFormula} m')
    print("\n")

elif (vMenu == 3):
    Distancia = float(input("Digite la distancia que ha recorrido el vehiculo: "))
    Velocidad = float(input("Digite la velocidad  del vehiculo: "))

    oFormula = Distancia / Velocidad

    print("\n")
    print(f't = d / v')
    print(f't = {Distancia} m / {Velocidad} m/s')
    print(f't = {oFormula} s')
    print("\n")

elif (vMenu == 4):
    vInicial = float(input("Digite la velocidad inicial del vehiculo: "))
    vFinal = float(input("Digite la velocidad final del vehiculo: "))
    Tiempo = float(input("Digite el tiempo del vehiculo: "))

    oFormula = (vFinal - vInicial) / Tiempo

    print("\n")
    print(f'a = vf - vi / t')
    print(f'a = {vFinal} m/s - {vInicial} m/s / {Tiempo} s')
    print(f'a = {round(oFormula)} m/s^2')
    print("\n")

else:
    print("Opcion invalida, digite de nuevo")