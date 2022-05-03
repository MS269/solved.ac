n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
max_val = max(max(*graph))
ans = 0


def dfs(x, y, c, tot):
    global ans

    if c == 4:
        ans = max(ans, tot)
        return

    if tot + max_val * (4 - c) <= ans:
        return

    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            dfs(nx, ny, c + 1, tot + graph[nx][ny])

    visited[x][y] = False


def rest(x, y):
    global ans

    tot = graph[x][y]
    cnt = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            tot += graph[nx][ny]
            cnt += 1

    if cnt == 4:
        ans = max(ans, tot)
    elif cnt == 5:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            tot -= graph[nx][ny]
            ans = max(ans, tot)
            tot += graph[nx][ny]


for i in range(n):
    for j in range(m):
        dfs(i, j, 1, graph[i][j])
        rest(i, j)

print(ans)
