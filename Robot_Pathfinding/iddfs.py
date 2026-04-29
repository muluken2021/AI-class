

from dls import dls

def iddfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    max_depth = rows * cols

    for limit in range(max_depth):
        result = dls(grid, start, goal, limit)

        if result is not None:
            return result

    return None