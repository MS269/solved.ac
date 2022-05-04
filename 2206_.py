from collections import deque


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[[-1, -1] for _ in range(m)] for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        x, y, z = q.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][z]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][z] == -1:
                if graph[nx][ny] == 0:
                    q.append((nx, ny, z))
                    visited[nx][ny][z] = visited[x][y][z] + 1
                if graph[nx][ny] == 1 and z < 1:
                    q.append((nx, ny, z + 1))
                    visited[nx][ny][z + 1] = visited[x][y][z] + 1

    return -1


print(bfs())
