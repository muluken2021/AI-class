from collections import deque

grid = [
    [0,0,0,0,0],
    [0,1,1,0,0],
    [0,0,0,1,0],
    [1,0,0,0,0],
    [0,0,1,0,0]
]

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set([start])

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        (x,y), path = queue.popleft()

        if (x,y) == goal:
            return path + [(x,y)]

        for dx, dy in directions:
            nx, ny = x+dx, y+dy

            if 0 <= nx < 5 and 0 <= ny < 5 and grid[nx][ny] == 0 and (nx,ny) not in visited:
                visited.add((nx,ny))
                queue.append(((nx,ny), path + [(x,y)]))

print(bfs((0,0), (4,4)))