import sys


input = sys.stdin.readline

r, c, m = map(int, input().split())
graph = [[0] * c for _ in range(r)]
dx, dy = (-1, 1, 0, 0), (0, 0, 1, -1)

for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    graph[x - 1][y - 1] = (s, d - 1, z)


def move():
    temp = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0:
                x, y = i, j
                s, d, z = graph[i][j]

                while s > 0:
                    x, y = x + dx[d], y + dy[d]

                    if 0 <= x < r and 0 <= y < c:
                        s -= 1
                    else:
                        x, y = x - dx[d], y - dy[d]

                        if d == 0 or d == 2:
                            d += 1
                        elif d == 1 or d == 3:
                            d -= 1

                if temp[x][y] == 0:
                    temp[x][y] = (graph[i][j][0], d, z)
                else:
                    if temp[x][y][2] < z:
                        temp[x][y] = (graph[i][j][0], d, z)

    return temp


ans = 0
for j in range(c):
    for i in range(r):
        if graph[i][j] != 0:
            ans += graph[i][j][2]
            graph[i][j] = 0
            break

    graph = move()

print(ans)
