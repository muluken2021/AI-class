def dls(grid, start, goal, limit):
    rows, cols = len(grid), len(grid[0])

    stack = [(start, 0)]
    visited = set()
    parent = {}

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while stack:
        (x, y), depth = stack.pop()

        if (x, y) == goal:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            path.reverse()
            return path

        if depth > limit:
            continue

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 0:
                    if (nx, ny) not in visited:
                        parent[(nx, ny)] = (x, y)
                        stack.append(((nx, ny), depth + 1))

    return None