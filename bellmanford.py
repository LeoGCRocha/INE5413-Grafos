from grafo import Grafo
import math
def distancias(dist):
    print("Vertex Distance from Source")
    for i in range(g.numVertices):
        print("%d : ; d : %s"%(i+1,str(dist[i])))
def bell(src):
    print(g.numVertices)
    dist = [math.inf] * g.numVertices
    dist[src] = 0
    for _ in range(g.numVertices- 1):
        for u, v, w in g.vertices:
            if dist[u] != math.inf and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    for u, v, w in g.vertices:
            if dist[u] != math.inf and dist[u] + w < dist[v]:
                    print("Ciclo negativo encontrado")
                    return
    distancias(dist)
g = Grafo("arquivos/caminho_minimo/caminho_minimo/fln_pequena.net")
bell(3)