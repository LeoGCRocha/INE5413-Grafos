from grafo import *
import math
def busca_em_largura(arquivo, vertice):
    meuGrafo = Grafo(arquivo)
    # configurando todos os vertices
    cv = [False] * meuGrafo.qtdVertices() # Determina se o vertice já foi visitado
    dv = [math.inf] * meuGrafo.qtdVertices() # Determina a distancia ate o vertice
    av = [None] * meuGrafo.qtdVertices()
    # configurando o vertice de origem
    cv[vertice - 1] = True
    dv[vertice - 1] = 0
    queue = [] # Lista de vertices
    queue.append(vertice)
    # Propagação das visitas
    nivel = 0
    # PROGRAMA COM ERRO VERIFICAR MELHOR ALGORITMO
    while len(queue) > 0:
        u = queue.pop()
        # Adicionar contador de niveis
        l = []
        for v in meuGrafo.vizinhos(u):
            if not cv[v-1]: # QUAL PROBLEMA NESTA LOGICA DO EXERCICIO
                cv[v - 1] = True
                dv[v - 1] = dv[u - 1] + 1
                av[v - 1] = u
                queue.insert(0, v)
        # CONTINUAR DAQUI CONTINUAR DAQUI CONTINUAR DAQUI
        # LOGICA PARA CADA NIVEL
        # TESTAR SE VALORES ESTÃO FUNCIONANDO
        print("%d:" % (nivel), end = ' ')
        print(l)
        nivel += 1
if __name__ == "__main__":
    vertice = 3 # vertice s que sera base para o problema
    busca_em_largura("arquivos/arvore_geradora_minima/agm_tiny.net", vertice)