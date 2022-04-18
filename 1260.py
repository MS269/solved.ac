from collections import deque


n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n + 1):
    graph[i].sort()


def dfs(x):
    visited[x] = True
    print(x, end=" ")

    for nx in graph[x]:
        if not visited[nx]:
            dfs(nx)


def bfs(x):
    q = deque([x])
    visited = set([x])

    while q:
        x = q.popleft()
        print(x, end=" ")

        for nx in graph[x]:
            if nx not in visited:
                q.append(nx)
                visited.add(nx)


dfs(v)
print()
bfs(v)
