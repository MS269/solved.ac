from collections import deque
import sys


input = sys.stdin.readline
inf = sys.maxsize

k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
visited = [[[-1] * (k + 1) for _ in range(w)] for _ in range(h)]
hx, hy = (2, 1, -1, -2, -2, -1, 1, 2), (1, 2, 2, 1, -1, -2, -2, -1)
mx, my = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 0

    while q:
        x, y, z = q.popleft()

        if x == h - 1 and y == w - 1:
            return visited[x][y][z]

        for i in range(8):
            nx, ny = x + hx[i], y + hy[i]

            if 0 <= nx < h and 0 <= ny < w and z + 1 <= k:
                if graph[nx][ny] == 0 and visited[nx][ny][z + 1] == -1:
                    q.append((nx, ny, z + 1))
                    visited[nx][ny][z + 1] = visited[x][y][z] + 1

        for i in range(4):
            nx, ny = x + mx[i], y + my[i]

            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 0 and visited[nx][ny][z] == -1:
                    q.append((nx, ny, z))
                    visited[nx][ny][z] = visited[x][y][z] + 1
    return -1


print(bfs())
