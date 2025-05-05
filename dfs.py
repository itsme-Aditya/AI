def dfs(graph, start):
    visited = [False] * len(graph)
    stack = [start]

    while stack:
        node = stack.pop()
        if visited[node] != True:
            print(node)
            visited[node] = True

            for neighbour in range(len(graph) - 1, -1, -1):
                if  graph[node][neighbour] == 1 and visited[neighbour] != True:
                    stack.append(neighbour)


graph = [
    # A  B  C  D  E  F
    [ 0, 1, 1, 0, 0, 0], # A
    [ 1, 0, 0, 1, 1, 0], # B
    [ 1, 0, 0, 0, 0, 1], # C
    [ 0, 1, 0, 0, 0, 0], # D
    [ 0, 1, 0, 0, 0, 1], # E
    [ 0, 0, 1, 0, 1, 0]  # F
]

dfs(graph, 0)
