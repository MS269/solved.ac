import heapq
import sys


input = sys.stdin.readline
inf = sys.maxsize

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())


def dijkstra(x):
    pq = []
    visited = [inf] * (n + 1)

    heapq.heappush(pq, (0, x))
    visited[x] = 0

    while pq:
        c, x = heapq.heappop(pq)

        if c > visited[x]:
            continue

        for nw, nx in graph[x]:
            nc = c + nw
            if nc < visited[nx]:
                visited[nx] = nc
                heapq.heappush(pq, (nc, nx))

    return visited


visited0 = dijkstra(1)
visited1 = dijkstra(v1)
visited2 = dijkstra(v2)

ans = min(visited0[v1] + visited1[v2] + visited2[n],
          visited0[v2] + visited2[v1] + visited1[n])

print(ans if ans < inf else -1)
