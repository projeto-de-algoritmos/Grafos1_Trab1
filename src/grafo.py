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





