import heapq

# Hardcoded initial and goal states
start = [[1, 2, 3],
         [4, 0, 6],
         [7, 5, 8]]

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

# Directions: up, down, left, right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def to_tuple(state):
    return (tuple(state[0]), tuple(state[1]), tuple(state[2]))

def a_star(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, []))
    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)
        key = to_tuple(current)
        if key in visited:
            continue
        visited.add(key)

        if current == goal:
            return path + [current]

        x, y = find_blank(current)
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [current[0][:], current[1][:], current[2][:]]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                if to_tuple(new_state) not in visited:
                    heapq.heappush(pq, (g + 1 + heuristic(new_state), g + 1, new_state, path + [current]))
    return None

def print_path(path):
    for i in range(len(path)):
        print("Step", i)
        for row in path[i]:
            print(row)
        print()

# Run the solver
solution = a_star(start)

# Output result
if solution:
    print_path(solution)
else:
    print("No solution found.")
