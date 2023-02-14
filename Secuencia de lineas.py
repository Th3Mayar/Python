#Escriba un programa que acepte una secuencia de líneas e imprima todas
#las líneas convertidas en mayúsculas. Deje una línea en blanco para indicar
#que ha finalizado la entrada de líneas.

sLineas = ''

while True:

    vCantLineas = int(input("Digite la cantidad de lineas: "))
    for item in range(vCantLineas):
        sLineas = sLineas + f' {item+1} - ' + input("\n ") + "\n"
    break

print(f"\n{sLineas.upper()}\n")
print("")