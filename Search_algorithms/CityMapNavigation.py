import heapq

graph = {
    "Arad": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],
    "Zerind": [("Arad", 75), ("Oradea", 71)],
    "Oradea": [("Zerind", 71), ("Sibiu", 151)],
    "Sibiu": [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu", 80)],
    "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
    "Rimnicu": [("Sibiu", 80), ("Pitesti", 97)],
    "Pitesti": [("Rimnicu", 97), ("Bucharest", 101)],
    "Timisoara": [("Arad", 118), ("Lugoj", 111)],
    "Lugoj": [("Timisoara", 111), ("Mehadia", 70)],
    "Mehadia": [("Lugoj", 70), ("Drobeta", 75)],
    "Drobeta": [("Mehadia", 75), ("Craiova", 120)],
    "Craiova": [("Drobeta", 120), ("Pitesti", 138)],
    "Bucharest": []
}

# heuristic (straight-line distance)
h = {
    "Arad": 366, "Zerind": 374, "Oradea": 380,
    "Sibiu": 253, "Fagaras": 176, "Rimnicu": 193,
    "Pitesti": 100, "Timisoara": 329, "Lugoj": 244,
    "Mehadia": 241, "Drobeta": 242, "Craiova": 160,
    "Bucharest": 0
}

def a_star(start, goal):
    pq = [(0 + h[start], 0, start, [])]  # (f, g, node, path)

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            return path + [node], g

        for neighbor, cost in graph[node]:
            heapq.heappush(pq, (g + cost + h[neighbor], g + cost, neighbor, path + [node]))

path, cost = a_star("Arad", "Bucharest")
print("Path:", path)
print("Cost:", cost)