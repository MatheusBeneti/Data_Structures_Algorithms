class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def addEdge(self, node, neighbor):
        if node not in self.adjacencyList:
            self.adjacencyList[node] = []
        self.adjacencyList[node].append(neighbor)

    def depthFirstSearch(self, startNode):
        visited = set()
        self._dfsUtil(startNode, visited)

    def _dfsUtil(self, node, visited):
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            neighbors = self.adjacencyList.get(node, [])
            for neighbor in neighbors:
                self._dfsUtil(neighbor, visited)

    def breadthFirstSearch(self, startNode):
        visited = set()
        queue = Queue()
        queue.enqueue(startNode)

        while not queue.isEmpty():
            node = queue.dequeue()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                neighbors = self.adjacencyList.get(node, [])
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.enqueue(neighbor)

graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(2, 0)
graph.addEdge(2, 3)
graph.addEdge(3, 3)

print("DFS:")
graph.depthFirstSearch(2)
print("\nBFS:")
graph.breadthFirstSearch(2)
