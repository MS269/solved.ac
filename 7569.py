from collections import deque


m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dx, dy, dz = (0, 0, -1, 1, 0, 0), (0, 0, 0, 0, -1, 1), (1, -1, 0, 0, 0, 0)


def bfs():
    q = deque()
    visited = [[[-1] * m for _ in range(n)] for _ in range(h)]

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    q.append((i, j, k))
                    visited[i][j][k] = 0
                elif graph[i][j][k] == -1:
                    visited[i][j][k] = 0

    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if graph[nx][ny][nz] == 0 and visited[nx][ny][nz] == -1:
                    q.append((nx, ny, nz))
                    visited[nx][ny][nz] = visited[x][y][z] + 1

    day = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if visited[i][j][k] == -1:
                    return -1
                day = max(day, visited[i][j][k])

    return day


print(bfs())
