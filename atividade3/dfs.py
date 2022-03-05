from grafo import Grafo
import math
g = Grafo("dfs.txt")
global visited
visited = [False]*g.qtdVertices()
dfsAnswer = []
def dfs(visited, node):
    if visited[node] == False:
        dfsAnswer.append(node + 1)
        visited[node] = True
        vizinhos = list(map(lambda x : x - 1, g.vizinhos(node + 1)))
        for v in vizinhos:
            dfs(visited,v)
node = 1 # vertice de origem
dfs(visited, node - 1)
print(dfsAnswer)