#Realizar un algoritmo que simule el funcionamiento de la alarma de
#un reloj digital permitiendo que el usuario indique en que hora deberá parar el
#reloj, mostrando el transcurrir del tiempo en pantalla y al final un mensaje de
#alerta.

import os
import time
import datetime
from datetime import datetime
import winsound
now = datetime.now()
now.hour
now.minute
now.second

os.system("cls")

def alarma():
    vHora = int(input("Ingrese la hora: "))
    vMinutos = int(input("Ingrese los minutos: ")) 
    vSegundos = int(input("Ingrese los segundos: "))

    for item1 in range(now.hour, 24):
        for item2 in range(now.minute, 60):
            for item3 in range(0, 60, 1):
                time.sleep(1)
                if (item3 < 10):
                    os.system("cls")
                    print(f"{item1}:{item2}:0{item3}")
                    
                elif (item3 >= 10):
                    os.system("cls")
                    print(f"{item1}:{item2}:{item3}")
                
                if ((vHora == item1) and (vMinutos == item2) and (vSegundos == item3)):
                    print(f"\nYa son las: {vHora}:{vMinutos}:{vSegundos}")
                    time.sleep(1)
                    for sonido in range(20):
                        sonido = 1000
                        duracion = 600
                        winsound.Beep(sonido, duracion) 
                    return 0
                else:
                    continue
alarma()