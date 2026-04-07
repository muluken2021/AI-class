import heapq

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])  # Manhattan

def astar(grid, start, goal):
    pq = [(0, start, [])]
    visited = set()

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while pq:
        f, node, path = heapq.heappop(pq)

        if node == goal:
            return path + [node]

        if node in visited:
            continue

        visited.add(node)

        for dx, dy in directions:
            nx, ny = node[0]+dx, node[1]+dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                g = len(path) + 1
                heapq.heappush(pq, (g + heuristic((nx,ny), goal), (nx,ny), path + [node]))

grid = [[0]*8 for _ in range(8)]
print(astar(grid, (1,1), (7,7)))