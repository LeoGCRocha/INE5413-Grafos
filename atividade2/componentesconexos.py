from grafo import Grafo
import math
g = Grafo("direcionado.net")
# DFS (Algoritmo 16)
def dfs(grafo, ordemvertices):
    # Definicoes iniciais
    cv = [False  for _ in range(0, grafo.qtdVertices())]
    tv, fv, av = [math.inf for _ in range(0, grafo.qtdVertices())], [math.inf for _ in range(0, grafo.qtdVertices())], [math.inf for _ in range(0, grafo.qtdVertices())]
    # Configurando o tempo de inicio
    tempo = 0
    for vertice in ordemvertices:
        if not cv[vertice]:
            # DFS-Visit Algoritmo 17
            cv, tv, fv, av, tempo = dfsvisit(grafo, cv, tv, fv, av, tempo, vertice)
    return cv, tv, av, fv
# DFS-Visit(Algoritmo 17)
def dfsvisit(grafo, cv, tv, fv, av, tempo, vertice):
    cv[vertice] = True
    tempo = tempo + 1
    tv[vertice] = tempo
    # Percorrendo vizinhos
    for u in grafo.vizinhos(vertice + 1):
        # Ajustando para retorno correto
        u = u - 1
        if cv[u] == False:
            av[u] = vertice
            cv, tv, fv, av, tempo = dfsvisit(grafo, cv, tv, fv, av, tempo, u)
    tempo = tempo + 1
    fv[vertice] = tempo
    return cv, tv, fv, av, tempo
# Definindo ordem
def definindoOrdem(f):
    maior = -math.inf
    ordem = []
    while(len(ordem) < len(f)):
        maior = -math.inf
        posicao = 0
        for i in range(0, len(f)):
            if (f[i] >= maior) and (f[i] != math.inf):
                maior = f[i]
                posicao = i
        f[posicao] = math.inf
        ordem.append(posicao)
    return ordem
def componentesConexos(grafo):
    # DFS Inicial
    # Os valores para antecessores deveriam ser somados a 1 para estarem ajustados
    ordem = [i for i in range(0, grafo.qtdVertices())]
    c, t, a ,f = dfs(grafo, ordem)
    # Grafo transposto
    grafo.transpor()
    # DFS-Ajustada com ordem de descrecente
    ordem = definindoOrdem(f) # FUNCIONANDO
    c, t, a, f = dfs(grafo ,ordem)
    componentes = []
    for i in range(0, len(a)):
        if(a[i] == math.inf):
            c = [i]
            proximo = [i]
            while(len(proximo) > 0):
                atual = proximo.pop()
                for index, value in enumerate(a):
                    if (value == atual):
                        proximo.append(index)
                        c.append(index)
            componentes.append(c)
    for componente in componentes:
        print(",".join(list(map(lambda x: str(x + 1), componente))))
componentesConexos(g)
