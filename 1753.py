import heapq
from sys import maxsize
import sys


input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
visited = [maxsize] * (v + 1)

for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))


def dijkstra(x):
    pq = []
    heapq.heappush(pq, (0, x))
    visited[x] = 0

    while pq:
        d, x = heapq.heappop(pq)

        if visited[x] < d:
            continue

        for nw, nx in graph[x]:
            nd = d + nw

            if nd < visited[nx]:
                heapq.heappush(pq, (nd, nx))
                visited[nx] = nd


dijkstra(k)

for i in range(1, v + 1):
    print(visited[i] if visited[i] != maxsize else "INF")
