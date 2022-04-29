from collections import deque


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)


def bfs():
    q = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return -1

    return max(map(max, graph)) - 1


print(bfs())
