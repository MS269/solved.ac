from collections import deque


n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs(x, y):
    q = deque()
    visited = [[-1] * m for _ in range(n)]

    q.append((x, y))
    visited[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == "L" and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    return max(map(max, visited))


ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            ans = max(ans, bfs(i, j))

print(ans)
