class Grafo:
    # IMPORTANTE
    # Grafo não direcionado, portanto é necessario adicionar a ligação em ambos os lados
    def __init__(self, arquivoRef = "arquivo.txt", vertices = 0, arestas = 0):
        self.__numVertices = vertices
        self.__numArestas = arestas
        self.__arquivoRef = arquivoRef 
        self.__matrizAdj = []
        self.__listAdj = []
        self.ajustandoGrafo()
    def lerArquivo(self):
        meuArquivo = open(self.__arquivoRef, 'r')
        return meuArquivo.readlines()
    def ajustandoGrafo(self):
        lista = self.lerArquivo()
        self.__numVertices = int(lista[0].split(" ")[1])
        # Construindo a lista de adjacencia
        self.__listAdj = [0]*self.__numVertices
        for a in range(1, self.__numVertices + 1):
            x,y = map(str, lista[a].split(" "))
            self.__listAdj[int(x) - 1] = [y.replace("\n", "")]
            # Adicionar aqui construção da matriz de adj
        for a in range(self.__numVertices + 2, len(lista)):
            x,y,z = map(str, lista[a].split(" ")) # x vertice 1, y vertice 2, z o peso
            # grafo não direcionado portando x -> y, y -> x
            self.__listAdj[int(x) - 1].append(int(y))
            self.__listAdj[int(y) - 1].append(int(x))
            # Fim da construção da lista de adj
            # Adicionar construção da matriz de adj
        for a in self.__listAdj:
            print(a)
    # def qtdVertices():
    def qtdVertices(self):
        return self.__numVertices
if __name__ == "__main__":
    meuGrafo = Grafo("arquivos/adjnoun.net")
    print(meuGrafo.qtdVertices())