import heapq
import sys


input = sys.stdin.readline
inf = sys.maxsize

m, n = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def dijkstra(x, y):
    pq = []
    visited = [[inf] * m for _ in range(n)]

    heapq.heappush(pq, (0, 0, 0))
    visited[0][0] = 0

    while pq:
        c, x, y = heapq.heappop(pq)

        if x == n - 1 and y == m - 1:
            break

        if c > visited[x][y]:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                nc = c + graph[nx][ny]

                if nc < visited[nx][ny]:
                    heapq.heappush(pq, (nc, nx, ny))
                    visited[nx][ny] = nc

    return visited[n - 1][m - 1]


print(dijkstra(0, 0))
