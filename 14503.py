n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
ans = 0


def dfs(x, y, d):
    global ans

    if not visited[x][y]:
        ans += 1
        visited[x][y] = True

    for i in range(4):
        nd = (d - i - 1) % 4
        nx, ny = x + dx[nd], y + dy[nd]

        if graph[nx][ny] == 0 and not visited[nx][ny]:
            dfs(nx, ny, nd)
            return

    nd = (d - 2) % 4
    nx, ny = x + dx[nd], y + dy[nd]

    if graph[nx][ny] == 1:
        return

    dfs(nx, ny, d)


dfs(r, c, d)

print(ans)
