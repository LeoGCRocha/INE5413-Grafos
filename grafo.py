import math
from os import replace
class Grafo:
    # IMPORTANTE
    def __init__(self, arquivoRef = "arquivo.txt", vertices = 0, arestas = 0):
        self.__numVertices = vertices
        self.__numArestas = arestas
        self.__arquivoRef = arquivoRef 
        self.__matrizAdj = []
        self.__direcionado = False
        self.__tipo = "txt"
        self.__Dic = {} # criacao do dicionário visando armazenar os itens a serem utilizados no grafo
        self.iniciarGrafo()

    def lerArquivo(self):
        meuArquivo = open(self.__arquivoRef, 'r')
        return meuArquivo.readlines()
    def iniciarGrafo(self):
        lista = self.lerArquivo()
        self.__numVertices = int(lista[0].split(" ")[1])
        # Adicionar vertices em um dicionario para o metodo rotulo(v)
        # CONTINUAR DAQUI !!!!!!!
        
        ## Dicionário    
        for i in range(1,self.__numVertices + 1): # loop inciado em 1 visando evitar o a captura do valor incorreto:  *vertices 6 
                                                  #                                                                   1 "Cafeteira" --> loop inicia aqui            
            lista1 = lista[i].replace("\n","").split(" ") # reposicionamento dos caracteres "\n" pelo espaço vazio a fim de evitar erros na tradução de itens para o dicionário
            self.__Dic[ int(lista1[0]) ] = lista1[1] # criação dos indices do dicionário, juntamento com os elementos
        
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
        if self.__tipo == "txt":
            self.construir_grafos_txt(lista)
    
    # retorna rótulo
    def retornaRotulo(self,v):
        return self.__Dic.get(v)

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
    # vizinhos
    def vizinhos(self, v):
        listaDeVizinhos = []
        for i in range(0, self.__numVertices):
            if self.__matrizAdj[v - 1][i] != math.inf:
                listaDeVizinhos.append(i + 1)
        return listaDeVizinhos
    # hasAresta
    def haAresta(self, u, v):
        val = self.__matrizAdj[u - 1][v - 1] # Duvida se deveria serr -1 ou não perguntar ao professor
        return True if val != math.inf else False
    # Peso de uma aresta
    def peso(self, u, v):
        return self.__matrizAdj[u - 1][v - 1] # Duvida se deveria ser -1 ou não, perguntar ao professor
    # def construir_grafos_grr()
    def construir_grafos_grr():
        pass

    # Grau de um vértice
    def grauVertice(self,v):
        grau = 0
        # Grafo direcionado:
        if self.__direcionado == True:
            pass
        
        # Grafo não direcionado:
        else:
            for i in range(0,self.__numVertices): # 
                if self.__matrizAdj[v - 1][i] != math.inf:
                    grau += 1
        return grau
if __name__ == "__main__":
    meuGrafo = Grafo("arquivos/arvore_geradora_minima/agm_tiny.net")
    # Testes do programa
    print(meuGrafo.qtdVertices())
    print(meuGrafo.haAresta(1,2))
    print(meuGrafo.vizinhos(1))
    print(meuGrafo.peso(1,3))
    print(meuGrafo.grauVertice(1))
    print(meuGrafo.retornaRotulo(1))
