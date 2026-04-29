import heapq

def ucs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    pq = [(0, start)]  # (cost, node)
    visited = set()
    parent = {}
    cost_so_far = {start: 0}

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while pq:
        cost, (x, y) = heapq.heappop(pq)

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
                new_cost = cost + 1

                if (nx, ny) not in cost_so_far or new_cost < cost_so_far[(nx, ny)]:
                    cost_so_far[(nx, ny)] = new_cost
                    heapq.heappush(pq, (new_cost, (nx, ny)))
                    parent[(nx, ny)] = (x, y)

    return None