import heapq
import sys


n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(x):
    pq = []
    visited = [sys.maxsize] * (n + 1)

    heapq.heappush(pq, (0, x))
    visited[x] = 0

    while pq:
        c, x = heapq.heappop(pq)

        if c > visited[x]:
            continue

        for nx, nw in graph[x]:
            nc = c + nw
            if nc < visited[nx]:
                heapq.heappush(pq, [nc, nx])
                visited[nx] = nc

    return visited


ans = [0] * (n + 1)
for i in range(1, n + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    ans[i] = go[x] + back[i]

print(max(ans))
