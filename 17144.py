r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
    if graph[i][0] == -1:
        top = i
        bottom = i + 1
        break


def diffuse():
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    diffused = [[0] * c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if graph[x][y] == 0 or graph[x][y] == -1:
                continue

            dust = graph[x][y] // 5

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                    diffused[nx][ny] += dust
                    diffused[x][y] -= dust

    for i in range(r):
        for j in range(c):
            graph[i][j] += diffused[i][j]


def clean_top():
    dx, dy = (0, -1, 0, 1), (1, 0, -1, 0)
    x, y, d = top, 1, 0
    prev = 0

    while True:
        nx, ny = x + dx[d], y + dy[d]

        if x == top and y == 0:
            break
        if not 0 <= nx < r or not 0 <= ny < c:
            d += 1
            continue

        graph[x][y], prev = prev, graph[x][y]
        x, y = nx, ny


def clean_bottom():
    dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
    x, y, d = bottom, 1, 0
    prev = 0

    while True:
        nx, ny = x + dx[d], y + dy[d]

        if x == bottom and y == 0:
            break
        if not 0 <= nx < r or not 0 <= ny < c:
            d += 1
            continue

        graph[x][y], prev = prev, graph[x][y]
        x, y = nx, ny


for _ in range(t):
    diffuse()
    clean_top()
    clean_bottom()

print(sum(map(sum, graph)) + 2)
