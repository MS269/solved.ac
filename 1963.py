from collections import deque


MAX = 10 ** 4

pn = [True] * MAX
pn[0] = pn[1] = False

for i in range(2, int(MAX ** 0.5) + 1):
    if not pn[i]:
        continue

    for j in range(i * i, MAX, i):
        pn[j] = False


def bfs(a, b):
    q = deque()
    visited = [-1] * MAX

    q.append(a)
    visited[a] = 0

    while q:
        a = q.popleft()

        if a == b:
            return visited[a]

        for i in range(1, 10):
            na = i * 1000 + a % 1000
            if pn[na] and visited[na] == -1:
                q.append(na)
                visited[na] = visited[a] + 1
        for i in range(10):
            na = a // 1000 * 1000 + i * 100 + a % 100
            if pn[na] and visited[na] == -1:
                q.append(na)
                visited[na] = visited[a] + 1
        for i in range(10):
            na = a // 100 * 100 + i * 10 + a % 10
            if pn[na] and visited[na] == -1:
                q.append(na)
                visited[na] = visited[a] + 1
        for i in range(10):
            na = a // 10 * 10 + i
            if pn[na] and visited[na] == -1:
                q.append(na)
                visited[na] = visited[a] + 1

    return "Impossible"


for _ in range(int(input())):
    a, b = map(int, input().split())

    print(bfs(a, b))
