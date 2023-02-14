#Tabla de multiplicar

Rep = True

while Rep == True:

    n1 = int(input("Digite el comienzo: "))
    n2 = int(input("Digite el final: "))

    if (n1 > 0 and n2 >0 and n1 < n2):
        Rep = False
        for item1 in range(1,n2+1):
            for item2 in range(1,14):
                print(f"{item1} x {item2} = {item1 * item2}")
    
    else:
        print("Has digitado un valor negativo o el primer numero es mayor que el segundo")