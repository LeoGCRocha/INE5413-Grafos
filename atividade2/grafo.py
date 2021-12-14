import math
from os import replace
class Grafo:
    # IMPORTANTE
    def __init__(self, arquivoRef = "arquivo.txt"):
        self.numVertices = 0
        self.__numArestas = 0
        self.__arquivoRef = arquivoRef 
        self.matrizAdj = []
        self.__direcionado = False
        self.__tipo = "txt"
        self.__Dic = {} # Criacao do dicionário visando armazenar os itens a serem utilizados no grafo
        self.vertices = []
        self.iniciarGrafo()
    # Leitura de arquivo
    def lerArquivo(self):
        meuArquivo = open(self.__arquivoRef, 'r')
        return meuArquivo.readlines()
    # Metodo de inicializacao principal
    def iniciarGrafo(self):
        lista = self.lerArquivo()
        self.numVertices = int(lista[0].split(" ")[1])
        # Dicionário    
        for i in range(1,self.numVertices + 1): # Loop inciado em 1 visando evitar o a captura do valor incorreto:  *vertices 6                                                                    1 "Cafeteira" --> loop inicia aqui            
            lista1 = lista[i].replace("\n","").split(" ") # Reposicionamento dos caracteres "\n" pelo espaço vazio a fim de evitar erros na tradução de itens para o dicionário
            self.__Dic[ int(lista1[0]) ] = lista1[1] # Criação dos indices do dicionário, juntamento com os elementos
        # Construção por matriz de adj
        # Construção de vetor
        if self.__arquivoRef.split(".")[1] == ".gr":
            self.__tipo = "gr"
            self.__numVertices 
        else:
            self.numVertices = int(lista[0].split(" ")[1])
        # Verifcando tipo de grafo
        # Construção da matriz tamanho |V| x |V| onde |V| é o numero de vertices.
        self.matrizAdj = [math.inf] * self.numVertices
        for i in range(0, self.numVertices):
            self.matrizAdj[i] = [math.inf] * self.numVertices
        if self.__tipo == "txt":
            self.construir_grafos_txt(lista)
        if self.__tipo == "gr":
            self.construir_grafos_grr()
    # Retorna rótulo
    def retornaRotulo(self,v):
        return self.__Dic.get(v)
    # def qtdVertices():
    def qtdVertices(self):
        return self.numVertices
    # def qtdArestas():
    def qtdArestas(self):
        return self.__numArestas
    # def construir_grafos_txt():
    def construir_grafos_txt(self, lista):
        # Não direcionado
        # Ida e Volta
        if lista[self.numVertices + 1].replace("\n","") == "*edges":
            for i in range(self.numVertices + 2, len(lista)):
               l = lista[i].replace("\n","").split(" ") # u,v,z
               u = int(l[0]) - 1 
               v = int(l[1]) - 1
               p = float(l[2])
               self.vertices.append([u,v,p])
               self.matrizAdj[u][v] = p
               self.matrizAdj[v][u] = p
        # Direcionado
        elif lista[self.numVertices + 1].replace("\n","") == "*arcs":
            self.__direcionado = True
            # Construindo grafo
            for i in range(self.numVertices + 2, len(lista)):
                l = lista[i].replace("\n", "").split(" ") # u, v, z
                u = int(l[0]) - 1
                v = int(l[1]) - 1
                p = float(l[2])
                self.vertices.append([u,v,p])
                self.matrizAdj[u][v] = p
    # Vizinhos
    def vizinhos(self, v):
        listaDeVizinhos = []
        # Vizinhos direcionados & não direcionados
        for i in range(0, self.numVertices):
            if self.matrizAdj[v - 1][i] != math.inf:
                listaDeVizinhos.append(i + 1)
        return listaDeVizinhos
    # hasAresta
    def haAresta(self, u, v):
        val = self.matrizAdj[u - 1][v - 1] # Duvida se deveria serr -1 ou não perguntar ao professor
        return True if val != math.inf else False
    # Peso de uma aresta
    def peso(self, u, v):
        return self.matrizAdj[u - 1][v - 1] # Duvida se deveria ser -1 ou não, perguntar ao professor
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
            for i in range(0,self.numVertices): # 
                if self.matrizAdj[v - 1][i] != math.inf:
                    grau += 1
        return grau   
    # Tranposto grafo
    def transpor(self):
        v2 = []
        for i in self.vertices:
            v2.append([i[1],i[0],i[2]])
            self.matrizAdj[i[0]][i[1]] =  math.inf
            self.matrizAdj[i[1]][i[0]] = i[2]
            
        self.vertices = v2