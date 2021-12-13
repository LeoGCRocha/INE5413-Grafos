from grafo import Grafo

def floydWarshall(grafo):
    
    # 5.4 pag. 57
    for k in range(grafo.qtdVertices()):
        for u in range(grafo.qtdVertices()):
            for v in range(grafo.qtdVertices()):
                grafo.matrizAdj[u][v] = min(grafo.matrizAdj[u][v],grafo.matrizAdj[u][k] + grafo.matrizAdj[k][v])
    
    # output
    for i in range(grafo.qtdVertices()):
        print(f"{i+1}: ", end="")
        print(*grafo.matrizAdj[i], sep=", ")

if __name__ == "__main__":
    grafo = Grafo("arquivos/caminho_minimo/caminho_minimo/fln_pequena.net") # Aqui vai o arquivo que sera utilizado como base
    floydWarshall(grafo)