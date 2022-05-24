from collections import deque


h, w = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs(x, y):
    q = deque([(x, y)])
    visited = set([(x, y)])
    cheese = []

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and (nx, ny) not in visited:
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                    visited.add((nx, ny))
                elif graph[nx][ny] == 1:
                    visited.add((nx, ny))
                    cheese.append((nx, ny))

    return cheese


hours = 0
count = sum(map(sum, graph))
prev = 0
while True:
    cheese = bfs(0, 0)

    if not cheese:
        break

    hours += 1
    count -= prev
    prev = len(cheese)

    for x, y in cheese:
        graph[x][y] = 0

print(hours)
print(count)
