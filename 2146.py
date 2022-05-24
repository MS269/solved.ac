from collections import deque
import sys


sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
inf = sys.maxsize

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def dfs(x, y, c):
    graph[x][y] = c
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny, c)


def bfs(c):
    q = deque()
    visited = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == c:
                q.append((i, j))
                visited[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                elif graph[nx][ny] != c:
                    return visited[x][y]


cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
            dfs(i, j, cnt)

ans = inf
for i in range(1, cnt + 1):
    ans = min(ans, bfs(i))

print(ans)
