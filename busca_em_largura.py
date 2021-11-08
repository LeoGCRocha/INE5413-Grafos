from grafo import Grafo

def busca_em_largura(grafo, vertice):
    visitados = [None] * grafo.qtdVertices()
    fila_de_vertices = [vertice]
    nivel = 0

    while len(fila_de_vertices):
        vestices_inicias = fila_de_vertices.copy()
        fila_de_vertices = []

        for vertice in vestices_inicias:
            visitados[vertice-1] = nivel
            vizinhos = [x for x in grafo.vizinhos(vertice) if visitados[x-1] == None]

            for i in vizinhos: visitados[i-1] = nivel+1
            fila_de_vertices = list(set().union(fila_de_vertices,vizinhos))
        
        print(f"{nivel}: {vestices_inicias}")
        
        nivel += 1
         
if __name__ == "__main__":
    grafo = Grafo("ent.txt")
    vertice_inicial = 3
    busca_em_largura(grafo, vertice_inicial)