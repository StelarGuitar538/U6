import numpy as np

class Secuencial:
    __numVertices: int
    __matriz: np.ndarray
    
    def __init__(self, numVertices):
        self.__numVertices = numVertices
        self.__matriz = np.zeros((numVertices, numVertices))
        
    def agregarArista(self, origen, destino, peso=1):
        if origen >= self.__numVertices or destino >= self.__numVertices:
            raise ValueError("El origen o el destino no es válido")
        self.__matriz[origen, destino] = peso
        self.__matriz[destino, origen] = peso
        
    def mostrar(self):
        for fila in self.__matriz:
            print(fila)
            
    def adyacentes(self, nodo):
        if nodo >= self.__numVertices:
            raise ValueError("nodo fuera de rango")
        else:
            adyacentes = []
            for i in range(self.__numVertices):
                if self.__matriz[nodo, i] != 0:
                    adyacentes.append(i)
            for j in range(len(adyacentes)):
                print(f"Nodo {nodo} tiene un adyacente {adyacentes[j]}")
                
    def grado(self, nodo): #cantidad de conexiones que tiene
        if nodo >= self.__numVertices:
            raise ValueError("nodo fuera de rango")
        else:
            print(f"el grado del nodo {nodo} es {np.sum(self.__matriz[nodo])}")
            
    def camino(self, inicio, fin):
        if inicio >= self.__numVertices or fin >= self.__numVertices:
            raise ValueError("El origen o el destino no es válido")
        else:
            visitados = [False] * self.__numVertices #crea una lista con la cantidad de vertices en false
            pila = [(inicio, [inicio])] #pila que contiene el nodo actual y el camino hasta el nodo actual
            
            while pila:
                nodoActual, caminoActual = pila.pop()
                print(f"camino {caminoActual} del nodo actual {nodoActual}")
                if nodoActual == fin:
                    return caminoActual
                
                if not visitados[nodoActual]:
                    visitados[nodoActual] = True
                    
                    for i in range(self.__numVertices):
                        if self.__matriz[nodoActual, i] == 1 and not visitados[i]:
                            pila.append((i, caminoActual + [i]))
                            
                            
    def BEP(self, nodo):
        visitados = [False] * self.__numVertices
        pila = [nodo]
        
        while pila:
            vertice = pila.pop() 
            if not visitados[vertice]:
                visitados[vertice] = True
                for i in range(self.__numVertices):
                    if self.__matriz[vertice][i] == 1 and not visitados[i]:
                        pila.append(i)
        return all(visitados)

    def BEA(self,nodo):
        visitados = [False] * self.__numVertices
        cola = [nodo]
        while cola:
            vertice = cola.pop(0)
            if not visitados[vertice]:
                visitados[vertice] = True
                for i in range(self.__numVertices):
                    if self.__matriz[vertice][i] == 1 and not visitados[i]:
                        cola.append(i)
        return all(visitados)

    def aciclico(self):
        visitados = [False] * self.__numVertices
        pila = [(0, -1)]

        while pila:
            nodoActual, padre = pila.pop()
            if not visitados[nodoActual]:
                visitados[nodoActual] = True
                for i in range(self.__numVertices):
                    if self.__matriz[nodoActual][i] == 1 and not visitados[i]:
                        pila.append((i, nodoActual))
                    elif self.__matriz[nodoActual][i] == 1 and i != padre:
                        return False
        return True
    
    


if __name__ == "__main__":
    g = Secuencial(5)
    
    g.agregarArista(0, 3)
    g.agregarArista(2, 4)
    g.agregarArista(1, 3)
    
    g.mostrar()
    g.adyacentes(2)
    g.grado(1)
    g.camino(0, 4)
    
    if g.BEP(0):
        print("grafo conexo")
    else:
        print("no es conexo")

    if g.aciclico():
        print("grafo aciclico")
    else:
        print("no es aciclico")
    
    
    
                