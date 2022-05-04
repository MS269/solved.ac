from sys import maxsize
import sys


sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
ans = maxsize


def dfs(x, y, c, broken):
    global ans

    if x == n - 1 and y == m - 1:
        ans = min(ans, c)
        return

    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if graph[nx][ny] == 0:
                dfs(nx, ny, c + 1, broken)
            if graph[nx][ny] == 1 and broken < 1:
                dfs(nx, ny, c + 1, broken + 1)

    visited[x][y] = False


dfs(0, 0, 1, 0)

print(ans if ans != maxsize else -1)
