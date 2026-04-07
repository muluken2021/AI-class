from collections import deque

word_list = {"hot","dot","dog","lot","log","cog"}

def neighbors(word):
    res = []
    for i in range(len(word)):
        for c in "abcdefghijklmnopqrstuvwxyz":
            new = word[:i] + c + word[i+1:]
            if new in word_list:
                res.append(new)
    return res

def word_ladder(start, goal):
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        word, path = queue.popleft()

        if word == goal:
            return path + [word]

        for nxt in neighbors(word):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [word]))

print(word_ladder("hit", "cog"))