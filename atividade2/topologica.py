from grafo import Grafo
import math
# Grafo baseado o demonstrado em aula pelo professor
g = Grafo("topologia.net")
def topologica(grafo):
    cv = [False] * grafo.qtdVertices()
    tv = [math.inf] * grafo.qtdVertices()  
    fv = [math.inf] * grafo.qtdVertices()
    av = [math.inf] * grafo.qtdVertices()
    tempo = 0
    o = []
    # DFS 
    for vertice in range(0, grafo.qtdVertices()):
        if not cv[vertice]:
            cv, tv, fv, av, tempo, o = dfsvisitot(grafo, cv, tv, fv, av, tempo, vertice, o)
    return o
def dfsvisitot(grafo, cv, tv, fv, av, tempo, vertice, o):
    cv[vertice] = True
    tempo = tempo + 1
    tv[vertice] = tempo
    # Percorrendo vizinhos
    for u in grafo.vizinhos(vertice + 1):
        # Ajustando para retorno correto
        u = u - 1
        if cv[u] == False:
            av[u] = vertice
            cv, tv, fv, av, tempo, o = dfsvisitot(grafo, cv, tv, fv, av, tempo, u, o)
    tempo = tempo + 1
    fv[vertice] = tempo
    o.insert(0, vertice)
    return cv, tv, fv, av, tempo, o
# Topologia
o = topologica(g)
dic = g.getDic()
print(" -> ".join(list(map(lambda x: dic[x + 1], o))))