from grafo import Grafo

import random

def Euler(grafo,vertices):
    # Primeira condição para ser um grafo euleriano: a quantidade de vértices de grau impar deve ser zero
    for i in range(vertices):
        if grafo.grauVertice(i) % 2 != 0:
            return("0")
    
    # vértice inicial aleatório a ser escolhido
    vinit = random.randint(0,vertices)

    # caminho realizado para completar o grafo
    caminho = []

    grafo = grafo.matrizAdj
   
    # O vértice atual é o vértice inicial
    vatual = vinit

    # o vértice inicial é o primeiro a ser visitado, dessa forma, usaremos um vetor para armazenar os vértices visitados
    visitados = [vinit]

    while(True):
        #Loop para visitar o vértice adjacente
        for i in range(vertices):
            if(grafo[vatual][i] == 1.0):
                # Colocando a aresta no vetor de caminho percorrido
                caminho.append([vatual,i])

                # Marcando a posição da aresta visitada com -1
                grafo[vatual][i] = -1
                grafo[i][vatual] = -1

                # Coloca o vértice visitado que foi visitado no vetor de vértices visitados
                visitados.append(i)

                # O próximo vértice a ser analisado será o vértice adjacente, reincia-se o processo de busca
                vatual = i
                break
            
        # Verfica se o vértice atual é o vértice incial, caso seja, finaliza o algoritimo,
        # o caminho foi realizado com sucesso, sem repetir as arestas percorridas
        if(vinit == vatual):
            break

    print("1")
    print(caminho)

if __name__ == "__main__":
    grafo = Grafo("arquivos/ciclo_euleriano/ciclo_euleriano/ContemCicloEuleriano.net") # Arquivo de input com o grafo a ser analisado
    vertices = 6 # quantidade de vértices
    Euler(grafo,vertices) # Instanciação da classe