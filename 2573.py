from collections import deque


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                elif graph[nx][ny] == 0:
                    melting[x][y] += 1


ans = 0
while True:
    visited = [[False] * m for _ in range(n)]
    melting = [[0] * m for _ in range(n)]
    splited = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                splited += 1
                bfs(i, j)

    for i in range(n):
        for j in range(m):
            graph[i][j] = max(0, graph[i][j] - melting[i][j])

    if splited == 0:
        ans = 0
        break
    if splited >= 2:
        break

    ans += 1


print(ans)
