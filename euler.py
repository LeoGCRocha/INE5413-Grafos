from grafo import Grafo
import random
def Euler(grafo):
    # Primeira condição: caso grau do vertice seja impar não existe ciclo portanto caminho []
    for i in range(grafo.qtdVertices()):
        if grafo.grauVertice(i) % 2 != 0:
            return(0, [])
    # Escolha um vertice inicial
    vinicial = 1
    # Colocando na pilha
    s = [vinicial]
    # Matriz adj
    arestas = grafo.matrizAdj.copy()
    t = []
    # -1 p/ marcada
    while len(s) > 0:
        # vertice do topo
        u = s[-1]
        inci = False
        for w in grafo.vizinhos(u):
            if arestas[u-1][w-1] != -1:
                arestas[u-1][w-1] = -1
                arestas[w-1][u-1] = -1
                s.append(w)
                inci = True
                break
        if not inci:
            s.pop()
            t.append(u)
    return(1, t)

if __name__ == "__main__":
    grafo = Grafo("arquivos/ciclo_euleriano/ciclo_euleriano/ContemCicloEuleriano.net") # Arquivo de input com o grafo a ser analisado
    resultado = Euler(grafo) # Instanciação da classe
    print(resultado[0])
    for x in range (0,len(resultado[1])-1):
        print(resultado[1][x], end=",")
    print(resultado[1][-1])