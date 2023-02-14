#Queremos realizar un programa que regule la cantidad de caracteres que se pueden
#escribir en una frase, siendo el limite de caracteres 60.

#We want to make a program that regulates the number of characters that can be
#write in a sentence, the character limit being 60.

def fMain():
    vFrase = input("Digite una frase: ")
    if len(vFrase) <= 60 and len(vFrase) > 0:
        print(f"\n\tLa frase era <{vFrase}>.\n")

    elif len(vFrase) > 60:
        print("\n\tEl maximo de caracteres permitidos es 60.\n")
        return fMain()
    
    else:
        print("\n\tNo has digitado ninguna frase.\n")
        return fMain()
fMain()