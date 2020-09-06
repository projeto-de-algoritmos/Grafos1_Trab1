import sys

class Vertice:
    def __init__(self, numero):
        self.numero = numero
        self.visitado = False
        self.vizinhos = []
        self.cores = []
        self.pai = None
        self.estado = False

    def add_vizinho(self, vizinho):
        if( (vizinho in self.vizinhos) == False):
            self.vizinhos.append(vizinho)
        else:
            print("Este vizinho JA existe!")

    def rm_vizinho(self, vizinho):
        if( (vizinho in self.vizinhos) == True):
            self.vizinhos.remove(vizinho)
        else:
            print("Este vizinho NAO  existe!")
    
    def add_estado(self, estado):
        self.estado = estado

    def add_visitado(self):
        self.visitado = True
    
    def imprime_visinhos(self):
        return self.vizinhos


class Grafo:
    def __init__(self):
        self.vertices = []
        self.numeroDeVertices = 0
        self.preenchidos = 0
    
    def add_vertice(self, vertice):
        self.vertices.append(vertice)
        self.numeroDeVertices +=1
    
    def add_vizinho_do_vertice(self, vertice_posicao ,vizinho):
        if(vertice_posicao != vizinho):
            self.vertices[vertice_posicao].add_vizinho(vizinho)
            self.vertices[vizinho].add_vizinho(vertice_posicao)

    
    def rm_vizinho_do_vertice(self, vertice_posicao ,vizinho):
        self.vertices[vertice_posicao].rm_vizinho(vizinho)
    
    def imprime_vertices(self):
        i = 0
        for no in self.vertices:
            print(str(no.imprime_visinhos()) + str(i))
            i+=1
    
    def imprime_tabela(self):
        if(self.preenchidos == 81):
            print("##################### SOLUCAO ####################")
            j=0
            for vertice in self.vertices:    
                print(vertice.numero, end="\t")
                if j in [8,17,26,35,44,53,62,71]:
                    print()
                j+=1

        else:
            print("ERRO: NAO FOI POSSIVEL RESOLVER")
            
        print()
            


