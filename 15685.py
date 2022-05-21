n = int(input())

graph = [[0] * 101 for _ in range(101)]
dx, dy = (1, 0, -1, 0), (0, -1, 0, 1)

for _ in range(n):
    x, y, d, g = map(int, input().split())
    graph[x][y] = 1

    curve = [d]
    for _ in range(g):
        for i in range(len(curve) - 1, -1, -1):
            curve.append((curve[i] + 1) % 4)

    for i in curve:
        x, y = x + dx[i], y + dy[i]
        if 0 <= x < 101 and 0 <= y < 101:
            graph[x][y] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i][j + 1] and graph[i + 1][j] and graph[i + 1][j + 1]:
            ans += 1

print(ans)
