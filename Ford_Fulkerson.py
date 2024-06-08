def find_path(graph, parent, source, sink):
    visited = set()
    queue = [source]
    visited.add(source)
    parent[source] = None

    while queue:
        current_node = queue.pop(0)
        for neighbor, capacity in graph.get(current_node, []):
            if neighbor not in visited and capacity > 0:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current_node

                if neighbor == sink:
                    return True

    return False

def ford_fulkerson(graph, source, sink):
    # Inicializa um dicionário para acompanhar os pais dos nós durante a busca de caminho
    parent_nodes = {}
    max_flow = 0

    # Enquanto houver um caminho do nó de origem para o nó de destino
    while find_path(graph, parent_nodes, source, sink):
        # Inicializa o fluxo do caminho como infinito
        path_flow = float("inf")
        current_node = sink

        # Encontra o fluxo mínimo no caminho encontrado
        while current_node != source:
            parent_node = parent_nodes[current_node]
            for neighbor, capacity in graph[parent_node]:
                if neighbor == current_node:
                    path_flow = min(path_flow, capacity)
                    break
            current_node = parent_node

        # Adiciona o fluxo do caminho ao fluxo máximo
        max_flow += path_flow

        # Atualiza as capacidades residuais do grafo
        current_node = sink
        while current_node != source:
            parent_node = parent_nodes[current_node]
            for i, (neighbor, _) in enumerate(graph[parent_node]):
                if neighbor == current_node:
                    graph[parent_node][i] = (neighbor, graph[parent_node][i][1] - path_flow)
                    break
            for i, (neighbor, _) in enumerate(graph[current_node]):
                if neighbor == parent_node:
                    graph[current_node][i] = (neighbor, graph[current_node][i][1] + path_flow)
                    break
            current_node = parent_node

    return max_flow


# Exemplo de uso com o seu grafo
graph = {
    1: [(2, 5), (3, 3)],
    2: [(1, 5), (3, 2)],
    3: [(1, 3), (2, 2)]
}

source = 1
sink = 3

max_flow = ford_fulkerson(graph, source, sink)
print(f"Fluxo máximo: {max_flow}")
