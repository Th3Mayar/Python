import os

#UTILICE EL MAPA DE ESPAÑA MOSTRADO EN EL EJEMPLO DE GRAFOS Y MEDIANTE EL CODE DE GRAFOS
#MOSTRAR UNA RUTA PRINCIPAL ENTRE SEVILLA Y CORUÑA Y 2 RUTAS ALTERNAS.

#Clase para definir vertices

############################################################################################

#USE THE MAP OF SPAIN SHOWN IN THE GRAPHIC EXAMPLE AND THROUGH THE GRAPHIC CODE
#SHOW A MAIN ROUTE BETWEEN SEVILLE AND CORUÑA AND 2 ALTERNATE ROUTES.

#Class to define vertices

class cVertice():

    #Constructor

    def __init__(self, i):
        self.uno = 2
        self.id = i
        self.visitando = False
        self.nivel = -1
        self.vecinos = []
    
    def fAgregarVecinos(self, v):
        if not v in self.vecinos:
            self.vecinos.append(v)

class cGrafica():

    def __init__(self):
        self.vertices = {}

    def fAgregarVertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = cVertice(v)
    
    def fAgregarArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].fAgregarVecinos(b)
            self.vertices[b].fAgregarVecinos(a)

def main():

    os.system("cls")
    
    g = cGrafica()
    #Mejor ruta entre sevilla y coruña

    Rutas = ['Sevilla', 'Jaen', 'Madrid', 'Valladolid', 'Coruña', 242, 335, 193, 356, 171, 'Sevilla', 'Granada', 'Murcia', 'Albacete', 'Madrid', 'Valladolid', 'Coruña']

    for r1 in Rutas:
        g.fAgregarVertice(r1)
    
    Rutas = ['Sevilla', 'Jaen', 'Jaen', 'Madrid', 'Madrid', 'Valladolid', 'Valladolid', 'Coruña', 242, 335, 335, 193, 193, 356, 356, 171, 'Sevilla', 'Granada', 'Granada', 'Murcia', 'Murcia', 'Albacete', 'Albacete', 'Madrid', 'Madrid', 'Valladolid', 'Valladolid', 'Coruña']
    
    for i in range(0, len(Rutas) -1, 2):
        g.fAgregarArista(Rutas[i], Rutas[i + 1])

    print("\nRUTAS MEDIANTE GRAFOS, LAS 3 ESTAN SEPARADAS POR TIPOS DE DATOS:\n")

    os.system("COLOR 02")

    print("""

            1 -  Esta en modo texto
            2 -  Esta en modo numeraciones
            3 -  Modo texto

        """)

    for v in g.vertices:

        print("\t\t", v, g.vertices[v].vecinos)

    print("\n\n")

main()

