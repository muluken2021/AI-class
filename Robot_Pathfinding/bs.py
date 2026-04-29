from collections import deque

def bs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    if start == goal:
        return [start]

    q1 = deque([start])
    q2 = deque([goal])

    visited1 = {start}
    visited2 = {goal}

    parent1 = {}
    parent2 = {}

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    meet = None

    while q1 and q2:
        # forward BFS
        for _ in range(len(q1)):
            x, y = q1.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                    if (nx, ny) not in visited1:
                        visited1.add((nx, ny))
                        parent1[(nx, ny)] = (x, y)
                        q1.append((nx, ny))

                        if (nx, ny) in visited2:
                            meet = (nx, ny)
                            break

        if meet:
            break

        # backward BFS
        for _ in range(len(q2)):
            x, y = q2.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                    if (nx, ny) not in visited2:
                        visited2.add((nx, ny))
                        parent2[(nx, ny)] = (x, y)
                        q2.append((nx, ny))

                        if (nx, ny) in visited1:
                            meet = (nx, ny)
                            break

        if meet:
            break

    if not meet:
        return None

    # reconstruct path
    path = []

    x, y = meet
    temp = (x, y)

    while temp in parent1:
        path.append(temp)
        temp = parent1[temp]
    path.append(start)
    path.reverse()

    temp = meet
    while temp in parent2:
        temp = parent2[temp]
        path.append(temp)

    return path