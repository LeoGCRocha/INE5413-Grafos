from grafo import Grafo
from queue import PriorityQueue
import math

def Dijsktra(grafo,origem):
    vs = grafo.qtdVertices() # quantidade de vertices utilzados
    grafo = grafo.matrizAdj.copy() # grafo a ser analisado
    visitado = [] # vetor de vértices visitados
    
    D = {v:float('inf') for v in range(vs)} # Dicionário contendo os caminhos dos vértices e os custos de tais caminhos
    D[origem] = 0

    pq = PriorityQueue()
    pq.put((0, origem))

    while not pq.empty():
        (dist, vertatual) = pq.get()
        visitado.append(vertatual)

        for adj in range(vs):
            if grafo[vertatual][adj] != math.inf:
                distancia = grafo[vertatual][adj]
                if adj not in visitado:
                    custo_ant = D[adj]
                    custo_aut = D[vertatual] + distancia
                    if custo_aut < custo_ant:
                        pq.put((custo_aut, adj))
                        D[adj] = custo_aut
    return D


if __name__ == "__main__":
    grafo = Grafo("arquivos/caminho_minimo/caminho_minimo/fln_pequena.net") # grafo a ser realizado o estudo
    vertice = 3 # int(input("vertice origem:\n")) vértice a ser realizada a busca de caminho minimo percorrido
    resultado = Dijsktra(grafo,vertice)
    print(resultado)

