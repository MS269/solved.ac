from collections import deque
import sys


input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    union = [(x, y)]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    union.append((nx, ny))

    return union


ans = 0
while True:
    visited = [[False] * n for _ in range(n)]
    unions = []

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union = bfs(i, j)
                if len(union) > 1:
                    unions.append(union)

    if not unions:
        break

    ans += 1

    for union in unions:
        pop = sum([graph[x][y] for x, y in union]) // len(union)
        for x, y in union:
            graph[x][y] = pop

print(ans)
