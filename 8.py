# Depth First Search
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Breadth First Search
def bfs(graph, start):
    visited = {start}
    queue = [start]

    for node in queue:
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("DFS Traversal:")
dfs(graph, 'A')

print("\nBFS Traversal:")
bfs(graph, 'A')
