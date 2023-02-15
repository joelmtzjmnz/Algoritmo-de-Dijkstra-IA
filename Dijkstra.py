class Vertice:
    def __init__(self, i):
        self.id = i
        self.visitado = False
        self.vecinos = []
        self.padre = None
        self.distancia = float('inf')

    def agregarVecino(self, v, p):
        if v not in self.vecinos:
            self.vecinos.append([v,p])

class Grafica:
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)

    def agregarArista(self, a, b, p):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b, p)
            self.vertices[b].agregarVecino(a, p)

    def imprimirGrafica(self):
        for v in self.vertices:
            print("La distancia del vertice "+str(v)+" es "+ str(self.vertices[v].distancia)+" llegando desde "+str(self.vertices[v].padre))

    def camino(self, a, b):
        camino = []
        actual = b
        while actual != None:
            camino.insert(0, actual)
            actual = self.vertices[actual].padre
        return [camino, self.vertices[b].distancia] 

    def minimo(self, lista):
        if len(lista) > 0:
            m = self.vertices[lista[0]].distancia
            v = lista[0]
            for e in lista:
                if m > self.vertices[e].distancia:
                    m = self.vertices[e].distancia
                    v = e
            
            return v

    def dijkstra(self, a):
        if a in self.vertices:
            self.vertices[a].distancia = 0
            actual = a
            noVisitados = []

            for v in self.vertices:
                if v != a:
                    self.vertices[v].distancia = float('inf')
                self.vertices[v].pare = None
                noVisitados.append(v)

            while len(noVisitados) > 0:
                for vecino in self.vertices[actual].vecinos:
                    if self.vertices[vecino[0]].visitado == False:
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]].distancia = self.vertices[actual].distancia + vecino[1]
                            self.vertices[vecino[0]].padre = actual

                self.vertices[actual].visitado = True
                noVisitados.remove(actual)

                actual = self.minimo(noVisitados)

        else:
            return False
            
def main():

    g = Grafica()
    g.agregarVertice("A")
    g.agregarVertice("B")
    g.agregarVertice("C")
    g.agregarVertice("D")
    g.agregarArista("A","B", 1)
    g.agregarArista("A","C", 2)
    g.agregarArista("A","D", 3)
    g.agregarArista("B", "C", 4)
    g.agregarArista("C", "D", 5)

    print("\n\nLa ruta más rápida por Dijkstra junto con su costo es: ")
    g.dijkstra("A")
    print(g.camino("A","D"))
    print("\nLos valores inales de la gráfica son los siguientes: ")
    g.imprimirGrafica()

main()