import heapq

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}
    parent = {}
    visited_order = []

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while open_list:
        _, current = heapq.heappop(open_list)
        visited_order.append(current)

        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return visited_order, path

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)

            if (0 <= nx < rows and 0 <= ny < cols and
                grid[nx][ny] == 0):

                new_cost = g_cost[current] + 1

                if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_cost
                    f_cost = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_cost, neighbor))
                    parent[neighbor] = current

    return [], None