#Queremos hacer un programa que cuente cuántos hashtags hay en un Tweet. Para lograr
#eso, tendríamos que recorrer todo el texto, encontrando cada carácter “#” para contarlo. 

vTexto = input("Digite un tweet: ")
Cont = 0

for item in vTexto[0:]:
    if item == '#':
        Cont = Cont + 1

print(f"\n\tEn el tweet hay <{Cont}> hashtags.\n")
print(type(f"{vTexto}"))
