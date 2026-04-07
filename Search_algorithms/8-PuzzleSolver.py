import heapq

goal = (1,2,3,4,5,6,7,8,0)

def heuristic(state):
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

def get_neighbors(state):
    idx = state.index(0)
    moves = []
    x, y = divmod(idx, 3)

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx*3 + ny
            lst = list(state)
            lst[idx], lst[new_idx] = lst[new_idx], lst[idx]
            moves.append(tuple(lst))

    return moves

def solve(start):
    pq = [(heuristic(start), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):
            heapq.heappush(pq, (g + 1 + heuristic(neighbor), g + 1, neighbor, path + [state]))

start = (1,2,3,4,0,5,6,7,8)
print(solve(start))