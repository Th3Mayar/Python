#Escribir un programa que cree un diccionario simulando una cesta de la compra. El
#programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que
#el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y
#el coste total, con el siguiente formato

import os
Carrito = {}
Coste = 0

while True:
    os.system("cls")
    Articulo = input('Introduce un artículo: ')
    Precio = float(input(f"Introduce el precio de articulo de clave [{Articulo}]: "))
    Carrito[Articulo] = Precio
    Salir = input('¿Quieres seguir añadiendo artículos a la lista (S/N)? ').upper()

    if Salir == 'S':
        pass

    elif Salir == 'N':
        break
    
    else:
        print("Opcion no valida")

os.system("pause")

for item, Precio in Carrito.items():
    print("Carrito de compras")
    print(f"""

        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
        ────────────────────────────────
        Articulo         Precio       
        ────────────────────────────────
        {item}             {Precio}

        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    """)

    Coste = Coste + Precio

print(f"""
                    Coste total: ${Coste}
    """)