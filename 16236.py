from collections import deque
from sys import maxsize


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (-1, 0, 0, 1), (0, -1, 1, 0)

sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            sx, sy = i, j
            graph[i][j] = 0


def bfs():
    global sx, sy, cnt

    q = deque([(sx, sy)])
    visited = [[-1] * n for _ in range(n)]
    visited[sx][sy] = 0
    min_dist = maxsize
    fish = []

    while q:
        x, y = q.popleft()

        if 0 < graph[x][y] < size:
            min_dist = min(min_dist, visited[x][y])
            if visited[x][y] == min_dist:
                fish.append((x, y))
            else:
                break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if not 0 <= nx < n or not 0 <= ny < n:
                continue
            if graph[nx][ny] > size or visited[nx][ny] != -1:
                continue

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    if fish:
        fish.sort()
        x, y = fish[0]
        sx, sy, cnt = x, y, cnt + 1
        graph[x][y] = 0
        return min_dist
    else:
        return -1


ans = 0
size, cnt = 2, 0
while True:
    sec = bfs()
    if sec == -1:
        break
    ans += sec

    if cnt == size:
        size += 1
        cnt = 0

print(ans)
