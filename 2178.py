from collections import deque


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        if x == n - 1 and y == m - 1:
            return visited[n - 1][m - 1]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


print(bfs(0, 0))
