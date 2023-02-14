#Escribir un programa que calcule la de vuelta que debe darse a un cliente luego de
#realizado una compra, los datos capturados deben ser positivos y tomar en cuenta
#que se captura el monto de la compra y el monto de pago dado por el cliente.

#Write a program that calculates the amount of return to be given to a customer after
#made a purchase, the data captured must be positive and take into account
#that captures the amount of the purchase and the amount of payment given by the customer.

import os

while True:
    os.system("cls")
    vMontoCompra = float(input("Digite el monto de la compra: "))
    vMontoPago = float(input("Digite el monto a pagar que dio el cliente: "))

    Total = vMontoPago - vMontoCompra

    if (vMontoCompra < 0 or vMontoPago < 0):
        print("Valores no admitidos, error al realizar la operacion")
        vMontoCompra = 0
        vMontoPago = 0
        os.system("pause")

    elif (vMontoPago < vMontoCompra):
        print("No posee el suficiente balance para pagar")
        vMontoCompra = 0
        vMontoPago = 0
        os.system("pause")

    else:
        Total = str(Total)
        print("\n" + Total + "\n")
        break
