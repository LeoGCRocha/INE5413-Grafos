from grafo import Grafo
import math
# Grafos
# Input:  Grafo dirigindo e ponderado G = (V, A, c), um vertice fonte s, vértice destino t
# Rede residual Gf = (V, Af, Cf)
g = Grafo("gb128.gr")
# f(u,v) -> 0
def ford_fulkerson():
    fluxo = 0
    # Matriz Residual
    while True:
        # Caminho Aumentate (p)
        caminho = edmonds_karp(g.n,g.s)
        if not caminho:
            break
        else:
            fluxo_cam = math.inf
            for i in range(len(caminho) - 1):
                fluxo_cam = min(g.matrizAdj[caminho[i]][caminho[i+1]], fluxo_cam)
            for i in range(len(caminho) - 1):
                g.matrizAdj[caminho[i]][caminho[i+1]] -= fluxo_cam 
            fluxo += fluxo_cam
    print(fluxo)
def edmonds_karp(fonte, destino): # s,t
    cv = [False] * g.numVertices # Conhecido
    av = [None] * g.numVertices # Ancestral
    cs = True # configurando o vertice de origem
    Q = [fonte]
    while len(Q) > 0:
        u = Q.pop()
        vizinhos = list(map(lambda x : x - 1, g.vizinhos(u + 1)))
        # print(vizinhos)
        for v in vizinhos:
            if not cv[v] and g.matrizAdj[u][v] > 0.0: # and > 0
                cv[v] = True
                av[v] = u
                if v == destino:
                    p = [destino]
                    w = destino
                    while w != fonte:
                        w = av[w]
                        p.append(w)
                    p.reverse()
                    return p 
                # Inserindo vizinho na fila
                Q.insert(0, v)
    return []
ford_fulkerson()