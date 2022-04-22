from collections import deque


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(x):
    q = deque([x])
    visited[x] = True
    c = 0

    while q:
        x = q.popleft()

        for nx in graph[x]:
            if not visited[nx]:
                q.append(nx)
                visited[nx] = True
                c += 1

    return c


print(bfs(1))
