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
    while len(queue) > 0:
        u = queue.pop()
        # Deve ser +1 ou não?
        for v in meuGrafo.vizinhos(u):
            cv[v - 1] = True
            # Continuar daqui  



if __name__ == "__main__":
    vertice = 3 # vertice s que sera base para o problema
    busca_em_largura("arquivos/arvore_geradora_minima/agm_tiny.net", vertice)