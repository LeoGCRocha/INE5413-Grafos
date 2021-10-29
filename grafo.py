class Grafo:
    # IMPORTANTE
    # Grafo não direcionado, portanto é necessario adicionar a ligação em ambos os lados
    def __init__(self, arquivoRef = "arquivo.txt", vertices = 0, arestas = 0):
        self.__numVertices = vertices
        self.__numArestas = arestas
        self.__arquivoRef = arquivoRef 
        self.__matrizAdj = []
        self.__direcionado = False
        self.iniciarGrafo()
    def lerArquivo(self):
        meuArquivo = open(self.__arquivoRef, 'r')
        return meuArquivo.readlines()
    def iniciarGrafo(self):
        lista = self.lerArquivo()
        self.__numVertices = int(lista[0].split(" ")[1])
        # Construção por matriz de adj
        # Construção de vetor
        if self.arquivoRef.split(".")[1] == ".gr":
            pass
            # Arquivo especial para outras partes
        else:
            self.__numVertices = int(lista[1].split(" ")[1])
        # Verifcando tipo de grafo
        # Não direcionado
        if lista[self.__numVertices + 2] == "*edges":
            pass
        # Direcionado
        elif lista[self.__numVertices + 2] == "*arcs":
            self.__direcionado = True
    # def qtdVertices():
    def qtdVertices(self):
        return self.__numVertices
    # def qtdArestas():
    def qtdArestas(self):
        pass
    # def construir_grafos_txt():
    def construir_grafos_txt():
        # continuar daqui 
        pass
    # def construir_grafos_grr()
    def construir_grafos_grr():
        pass

if __name__ == "__main__":
    meuGrafo = Grafo("arquivos/adjnoun.net")
    print(meuGrafo.qtdVertices())