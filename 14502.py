from collections import deque
from copy import deepcopy
from itertools import combinations


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)

empty = []
virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))


def bfs(walls):
    temp_graph = deepcopy(graph)

    for x, y in walls:
        temp_graph[x][y] = 1

    q = deque(virus)

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if temp_graph[nx][ny] == 0:
                    q.append((nx, ny))
                    temp_graph[nx][ny] = 2

    safe_area = 0
    for row in temp_graph:
        safe_area += row.count(0)

    return safe_area


ans = 0
for walls in combinations(empty, 3):
    ans = max(ans, bfs(walls))

print(ans)
