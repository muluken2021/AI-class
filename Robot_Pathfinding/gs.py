import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def gs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    pq = [(heuristic(start, goal), start)]
    visited = set()
    parent = {}

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while pq:
        _, (x, y) = heapq.heappop(pq)

        if (x, y) == goal:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            path.reverse()
            return path

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                if (nx, ny) not in visited:
                    parent[(nx, ny)] = (x, y)
                    heapq.heappush(pq, (heuristic((nx, ny), goal), (nx, ny)))

    return None