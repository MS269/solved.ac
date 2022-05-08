from collections import deque


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    x = q.popleft()

    for nx in graph[x]:
        indegree[nx] -= 1

        if indegree[nx] == 0:
            q.append(nx)

    print(x, end=" ")
