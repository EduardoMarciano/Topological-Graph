# Implementação do Grafo e do Vêrtice com a utilização de POO  
class Graph:
    def __init__(self):
        self.vertices = []
        self.vertices_id = []
        
    def addVertex(self, v, creditos):

        newVertex = Vertex(v, creditos)
        self.vertices.append(newVertex)
        self.vertices_id.append(newVertex.id)
    
    def getVertex(self,n):
        for v in self.vertices:
            if v.id == n:
                return v

    def getVertices(self):
        return self.vertices
        
class Vertex:
    def __init__(self, num, creditos):
        self.id = num
        self.creditos = creditos
        self.saida = []
        self.incidencia = []
        #Numero de matérias com pré-requisitos diretos
        self.dependencia = 0
    
    def addSaida(self,nbr, peso):
        self.saida.append((nbr, peso))

    def getSaida(self):
        return self.saida
    
    def addIncidencia(self,nbr):
        self.incidencia.append(nbr)
        self.dependencia+= 1          
    
    def getIncidencia(self):
        return self.incidencia
    
    def getSaida(self):
        return self.saida