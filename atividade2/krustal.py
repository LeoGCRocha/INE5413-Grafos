from grafo import Grafo

def kruskal(grafo):
    arestas = grafo.arestas()
    arestas.sort(key = lambda x: x[2])
    conjuntos = [-1] * (grafo.qtdVertices())
    resultado = []

    for aresta in arestas:
        u = aresta[0]
        v = aresta[1]
        conjuntos, su = conjuntoEncontrar(conjuntos, u)
        conjuntos, sv = conjuntoEncontrar(conjuntos, v)
        if (su != sv):
            resultado.append(aresta)
            conjuntos = conjuntoAddUniao(conjuntos, su, sv)
    return resultado

def conjuntoEncontrar(conjuntos, u):
    x = u
    v = False
        
    while (conjuntos[x] >= 0):
        x = conjuntos[x]
 
    while (u != x):        
        v, conjuntos[u], u = conjuntos[u], x, v
    
    return conjuntos, x

def conjuntoAddUniao(conjuntos, u, v):
    if (conjuntos[u] >= conjuntos[v]):
        conjuntos[v] += conjuntos[u]
        conjuntos[u] = v
        return conjuntos
    
    conjuntos[u] += conjuntos[v]
    conjuntos[v] = u
    return conjuntos

if __name__ == "__main__":
    grafo = Grafo("../arquivos/caminho_minimo/caminho_minimo/fln_pequena.net")
    resultado = kruskal(grafo)
    
    print(sum([i[2] for i in resultado]))
    for i in resultado:
        print(f'{i[0]+1}-{i[1]+1}, ',end="")
    print()
    