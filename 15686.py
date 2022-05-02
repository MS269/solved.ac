from collections import deque
from itertools import combinations
from sys import maxsize


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)


def bfs(open):
    q = deque()
    visited = [[-1] * n for _ in range(n)]
    dist = 0

    for x, y in open:
        q.append((x, y))
        visited[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                elif graph[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    dist += visited[nx][ny]

    return dist


shops = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            shops.append((i, j))
            graph[i][j] = 0

ans = maxsize
for open in combinations(shops, m):
    ans = min(ans, bfs(open))

print(ans)
