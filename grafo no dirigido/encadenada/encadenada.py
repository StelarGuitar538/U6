from nodo import Nodo

class Encadenada:
    __numVertices: int
    __matriz: list
    
    def __init__(self, numVertices):
        self.__numVertices = numVertices
        self.__matriz = [None for _ in range(numVertices) ]
        
    
    def agregarArista(self, origen, destino, peso=1):
        if origen >= self.__numVertices or destino >= self.__numVertices:
            raise ValueError("El origen o el destino no es válido")
        self.__matriz[origen][destino] = peso
        self.__matriz[destino, origen] = peso
        
    def mostrar(self):
        for fila in self.__matriz:
            print(fila)
            
            
if __name__ == "__main__":
    g = Encadenada(5)
    
    """g.agregarArista(0, 3)
    g.agregarArista(2, 4)
    g.agregarArista(1, 3)"""
    
    g.mostrar()
        
        
    