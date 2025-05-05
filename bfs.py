def bfs(graph, start):
    visited = [False] * len(graph)
    queue = [start]

    while queue:
        node = queue.pop(0)
        if not visited[node]:
            print(node)
            visited[node] = True

            for neighbour in range(len(graph)):
                if graph[node][neighbour] == 1 and not visited[neighbour]:
                    queue.append(neighbour)


graph = [
    # A  B  C  D  E  F
    [ 0, 1, 1, 0, 0, 0], # A
    [ 1, 0, 0, 1, 1, 0], # B
    [ 1, 0, 0, 0, 0, 1], # C
    [ 0, 1, 0, 0, 0, 0], # D
    [ 0, 1, 0, 0, 0, 1], # E
    [ 0, 0, 1, 0, 1, 0]  # F
]

bfs(graph, 0)
