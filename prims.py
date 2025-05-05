graph = [
    # A   B   C   D   E   F
    [ 0,  2,  3,  0,  0,  0],  # A
    [ 2,  0,  0,  5,  4,  0],  # B
    [ 3,  0,  0,  0,  0,  7],  # C
    [ 0,  5,  0,  0,  0,  0],  # D
    [ 0,  4,  0,  0,  0,  6],  # E
    [ 0,  0,  7,  0,  6,  0]   # F
]

def prims():
    visited = [False] * len(graph)
    visited[0] = True
    mincost = 0

    for k in range(0, len(graph) - 1):
        row = col = -1
        m = 9999

        for i in range(len(graph)):
            if visited[i]:

                for j in range(len(graph)):
                    if not visited[j] and graph[i][j]:
                        if m > graph[i][j]:
                            m = graph[i][j]
                            row, col = i, j
        if row != -1 and col != -1:
            print(f"{row}----->{col} : {m}")
            visited[col] = True
            mincost += m
    print("Minimum cost: ", mincost)


prims()
