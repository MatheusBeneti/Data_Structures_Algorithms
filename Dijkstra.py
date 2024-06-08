import heapq 

def dijkstra(grafo, origem):

  #Inicializa todas as distancias com infinito
  distancias = {vertice: float('inf') for vertice in grafo} 
  distancias[origem] = 0
  predecessor = {vertice: None for vertice in grafo}

  #Fila de prioridades para armazenar vértices a serem explorados
  fila_prioridade = [(0, origem)]

  while fila_prioridade:
    #Remove o vértice com menor distância da fila
    atual, vertice_atual = heapq.heappop(fila_prioridade)

    #Se a distância mínima para o vértice atual já foi encontrada, ignora
    if atual > distancias[vertice_atual]:
      continue

    #Explora os vizinhos do vértice atual
    for vizinho, peso in grafo[vertice_atual]:
      nova_distancia = atual + peso

      #Se a nova distância for menor que a distância atual do vizinho, atualiza
      if nova_distancia < distancias[vizinho]:
        distancias[vizinho] = nova_distancia
        predecessor[vizinho] = vertice_atual

        #Adiciona o vizinho à fila de prioridades com sua nova distância
        heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

  return distancias, predecessor



grafo = {
    'A': [('B', 5), ('C', 1)],
    'B': [('A', 5), ('C', 2), ('D', 4)],
    'C': [('A', 1), ('B', 2), ('D', 7)],
    'D': [('B', 4), ('C', 7)],
}

origem = 'A'
distancias, pais = dijkstra(grafo, origem)

for destino, distancia in distancias.items():
  caminho = [destino]
  atual = pais[destino]
  while atual:
    caminho.append(atual)
    atual = pais[atual]
  caminho.reverse()
  print(f"De {origem} para {destino}: {distancia} ({caminho})")

