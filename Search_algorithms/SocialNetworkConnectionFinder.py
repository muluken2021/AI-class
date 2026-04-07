graph = {
    "Alice": ["Bob", "Claire"],
    "Bob": ["Alice", "Dan"],
    "Claire": ["Alice", "Eve"],
    "Dan": ["Bob"],
    "Eve": ["Claire"]
}

def find_connection(start, goal):
    from collections import deque
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        person, path = queue.popleft()

        if person == goal:
            return path + [person]

        for friend in graph[person]:
            if friend not in visited:
                visited.add(friend)
                queue.append((friend, path + [person]))

print(find_connection("Alice", "Eve"))