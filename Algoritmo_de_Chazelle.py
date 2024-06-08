def chazelle_mst(graph):

    uf = UnionFind(graph.keys())
    pq = PriorityQueue()
    mst = []

    #Adiciona todas as arestas à fila de prioridades
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            pq.add((weight, vertex, neighbor))

    #Lista para armazenar as arestas da AGM

    #Loop até que todos os vértices estejam conectados
    while len(mst) < len(graph) - 1:
        #Remove a aresta de menor custo da fila de prioridades
        edge = pq.pop()
        if edge is None:
            break
        weight, vertex1, vertex2 = edge

        #Se os vértices da aresta não estão no mesmo componente, adiciona a aresta à AGM e une os componentes
        if uf.find(vertex1) != uf.find(vertex2):
            mst.append((vertex1, vertex2))
        uf.union(vertex1, vertex2)

    return mst

class UnionFind:
  def __init__(self, nodes):
    self.parents = {node: node for node in nodes}
    self.ranks = {node: 0 for node in nodes}

  def find(self, node):
    if self.parents[node] != node:
      self.parents[node] = self.find(self.parents[node])
    return self.parents[node]

  def union(self, node1, node2):
    parent1 = self.find(node1)
    parent2 = self.find(node2)

    if parent1 == parent2:
      return

    if self.ranks[parent1] < self.ranks[parent2]:
      self.parents[parent1] = parent2
    else:
      self.parents[parent2] = parent1
      if self.ranks[parent1] == self.ranks[parent2]:
        self.ranks[parent1] += 1

class PriorityQueue:
  def __init__(self):
    self.heap = []

  def add(self, item):
    self.heap.append(item)
    self._heapify_up()

  def pop(self):
    if len(self.heap) == 0:
      return None

    item = self.heap[0]
    self.heap[0] = self.heap[-1]
    self.heap.pop()
    self._heapify_down(0)

    return item

  def _heapify_up(self):
    i = len(self.heap) - 1
    while i > 0:
      parent = (i - 1) // 2
      if self.heap[i] < self.heap[parent]:
        self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
        i = parent
      else:
        break

  def _heapify_down(self, i):
    while i < len(self.heap):
      left = 2 * i + 1
      right = 2 * i + 2

      if left < len(self.heap) and self.heap[left] < self.heap[i]:
        smallest = left
      else:
        smallest = i

      if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
        smallest = right

      if smallest != i:
        self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
        i = smallest
      else:
        break

graph = {
    'A': [('B', 1), ('C', 5)],
    'B': [('A', 2), ('C', 6), ('D', 9)],
    'C': [('A', 3), ('B', 7), ('D', 10)],
    'D': [('B', 4), ('C', 8)]
}

agm = chazelle_mst(graph)

print(agm)

