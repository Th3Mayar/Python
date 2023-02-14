# Escriba un programa que simule administrar una cuenta de banco
# usando la siguiente nomenclatura para las transacciones:

    #a. D – Débito – Suma
    #b. C – Crédito – Resta
    #c. El programa finaliza cuando se digite la letra S al capturar la descripción de la actividad a realizar.

# Write a program that simulates managing a bank account
# using the following nomenclature for transactions:

    #a. D – Debit – Sum
    #b. C – Credit – Subtraction
    #c. The program ends when the letter S is entered when entering the description of the activity to be carried out.

import os
import time
os.system("cls")

while True:

    vCuenta = float(input(f"Digite el monto a depositar para abrir la cuenta: "))

    if(vCuenta < 500):

        print("Lo siento, el minimo de deposito para abrir su cuenta es de 500")

    else:

        break

while True: 

        os.system("cls")
        print("""

        ELIJA UNA OPCION

                M - Saldo de Cuenta
                D - Agregar saldo a su cuenta
                C - Retirar su monto
                S - Salir

        """)
        Op = input("Digite una opcion: ").upper()

        if(Op == 'M'):
            print("\nProcesando orden...")
            time.sleep(2)
            print("\nSolicitando informacion...")
            time.sleep(2)
            print(f"Su cuenta posee un saldo de: RD${vCuenta}")

        elif(Op == 'D'):
            vDeposito = float(input("Agregue un saldo a depositar: "))
            print("\nProcesando orden...")
            time.sleep(2)
            vCuenta = vCuenta + vDeposito
            print("\nOrden Realizada exitosamente.\n")

        elif(Op == 'C'):
            vRetirar = float(input("Digite el monto a retirar: "))
            print("\nProcesando orden...")
            time.sleep(2)

            if (vRetirar > vCuenta):
                print("Transaccion invalida, no posee saldo suficiente")

            else:
                vConfirmacion = input(f"Desea retirar RD${vRetirar} (S/N)? ").upper()
                if (vConfirmacion == 'S'):
                    vCuenta = vCuenta - vRetirar
                    print("\nProcesando orden...")
                    time.sleep(2)
                    print("\nOrden Realizada exitosamente\n")

                elif (vConfirmacion == 'N'):
                    print("\nProcesando orden...")
                    time.sleep(2)
                    print("Transaccion cancelada")

        elif(Op == 'S'):
            print("Gracias por preferirnos")
            break

        else:
            print("\nEsta opcion no es valida, intente con otra...")
        os.system("\npause")