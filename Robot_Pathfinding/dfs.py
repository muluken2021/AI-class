def dfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    stack = [start]
    visited = set([start])
    parent = {}

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while stack:
        x, y = stack.pop()

        if (x, y) == goal:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            path.reverse()
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < rows and 0 <= ny < cols and
                grid[nx][ny] == 0 and (nx, ny) not in visited):

                stack.append((nx, ny))
                visited.add((nx, ny))   # ✅ mark early
                parent[(nx, ny)] = (x, y)

    return None