from grafo import Grafo

def Euler(grafo,vertices):
    # Primeira condição para ser um grafo euleriano: a quantidade de vértices de grau impar deve ser zero
    for i in range(vertices):
        if grafo.GrauVertice(i) % 2 != 0:
            print('0')
            break
    else:
    # Caso seja euleriano, uma solução para percorrer o grafo é ...
        pass




if __name__ == "__main__":
    grafo = Grafo("arquivos/ciclo_euleriano/ciclo_euleriano/SemCicloEuleriano.net") # Arquivo de input com o grafo a ser analisado
    vertices = 6 # quantidade de vértices
    Euler(grafo,vertices) # Instanciação da classe