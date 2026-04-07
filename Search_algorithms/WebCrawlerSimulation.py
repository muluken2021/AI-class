graph = {
    "Home": ["About", "Products"],
    "About": ["Team", "Careers"],
    "Products": ["Product1", "Product2"],
    "Team": [],
    "Careers": ["Apply"],
    "Product1": [],
    "Product2": [],
    "Apply": []
}

from collections import deque

def crawl(start, target):
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        node, path = queue.popleft()

        if node == target:
            return path + [node]

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [node]))

print(crawl("Home", "Apply"))