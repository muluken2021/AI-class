
import heapq

graph = {
    "A": [("B",1), ("C",4)],
    "B": [("D",2), ("E",5)],
    "C": [("F",3)],
    "D": [("G",1)],
    "E": [("G",2)],
    "F": [("G",5)],
    "G": []
}

def ucs(start, goal):
    pq = [(0, start, [])]

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path + [node], cost

        for neighbor, c in graph[node]:
            heapq.heappush(pq, (cost + c, neighbor, path + [node]))

print(ucs("A", "G"))