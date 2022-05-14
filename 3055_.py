from collections import deque


r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [[-1] * c for _ in range(r)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs():
    q = deque()

    for i in range(r):
        for j in range(c):
            if graph[i][j] == "*":
                q.appendleft((i, j))
                visited[i][j] = 0
            elif graph[i][j] == "S":
                q.append((i, j))
                visited[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not 0 <= nx < r or not 0 <= ny < c:
                continue
            if visited[nx][ny] != -1:
                continue
            if graph[nx][ny] == "*" or graph[nx][ny] == "X":
                continue
            if graph[nx][ny] == "D" and graph[x][y] == "*":
                continue
            if graph[nx][ny] == "D" and graph[x][y] == "S":
                return visited[x][y] + 1

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
            graph[nx][ny] = graph[x][y]

    return "KAKTUS"


print(bfs())
