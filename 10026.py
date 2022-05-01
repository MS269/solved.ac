import sys


sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = [list(input()) for _ in range(n)]
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)


def normal_dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                normal_dfs(nx, ny)


def abnormal_dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if graph[nx][ny] == graph[x][y]:
                abnormal_dfs(nx, ny)
            elif graph[nx][ny] == "R" and graph[x][y] == "G":
                abnormal_dfs(nx, ny)
            elif graph[nx][ny] == "G" and graph[x][y] == "R":
                abnormal_dfs(nx, ny)


normal_ans = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            normal_dfs(i, j)
            normal_ans += 1

abnormal_ans = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            abnormal_dfs(i, j)
            abnormal_ans += 1

print(normal_ans, abnormal_ans)
