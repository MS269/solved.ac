import sys


sys.setrecursionlimit(10 ** 6)

dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)


def dfs(x, y):
    graph[x][y] = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                dfs(nx, ny)


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    ans = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                ans += 1

    print(ans)
