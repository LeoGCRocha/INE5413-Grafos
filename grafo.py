import math
class Grafo:
    # IMPORTANTE
    # Grafo não direcionado, portanto é necessario adicionar a ligação em ambos os lados
    def __init__(self, arquivoRef = "arquivo.txt", vertices = 0, arestas = 0):
        self.__numVertices = vertices
        self.__numArestas = arestas
        self.__arquivoRef = arquivoRef 
        self.__matrizAdj = []
        self.__direcionado = False
        self.__tipo = "txt"
        self.iniciarGrafo()
    def lerArquivo(self):
        meuArquivo = open(self.__arquivoRef, 'r')
        return meuArquivo.readlines()
    def iniciarGrafo(self):
        lista = self.lerArquivo()
        self.__numVertices = int(lista[0].split(" ")[1])
        # Adicionar vertices em um dicionario para o metodo rotulo(v)
        # CONTINUAR DAQUI !!!!!!!
        
        # Construção por matriz de adj
        # Construção de vetor
        if self.__arquivoRef.split(".")[1] == ".gr":
            self.__tipo = "gr"
            pass
            # Arquivo especial para outras partes
        else:
            self.__numVertices = int(lista[0].split(" ")[1])
        # Verifcando tipo de grafo
        # Construção da matriz tamanho |V| x |V| onde |V| é o numero de vertices.
        self.__matrizAdj = [math.inf] * self.__numVertices
        for i in range(0, self.__numVertices):
            self.__matrizAdj[i] = [math.inf] * self.__numVertices
        print(self.__matrizAdj)
        if self.__tipo == "txt":
            self.construir_grafos_txt(lista)
        print(self.__matrizAdj)
    # def qtdVertices():
    def qtdVertices(self):
        return self.__numVertices
    # def qtdArestas():
    def qtdArestas(self):
        pass
    # def construir_grafos_txt():
    def construir_grafos_txt(self, lista):
        # Não direcionado
        # Ida e Volta
        if lista[self.__numVertices + 1].replace("\n","") == "*edges":
            for i in range(self.__numVertices + 2, len(lista)):
               l = lista[i].replace("\n","").split(" ") # u,v,z
               u = int(l[0]) - 1 
               v = int(l[1]) - 1
               p = float(l[2])
               self.__matrizAdj[u][v] = p
               self.__matrizAdj[v][u] = p
        # Direcionado
        elif lista[self.__numVertices + 1] == "*arcs":
            self.__direcionado = True
    # hasAresta
    def haAresta(self, u, v):
        val = self.__matrizAdj[u - 1][v - 1]
        return True if val != math.inf else False
    # Peso de uma aresta
    def peso(self, u, v):
        return self.__matrizAdj[u - 1][v - 1]
    # def construir_grafos_grr()
    def construir_grafos_grr():
        pass
if __name__ == "__main__":
    meuGrafo = Grafo("arquivos/arvore_geradora_minima/agm_tiny.net")
    print(meuGrafo.qtdVertices())