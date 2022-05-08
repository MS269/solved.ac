n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
dx, dy = (0, 0, 0, -1, 1), (0, 1, -1, 0, 0)
dice = [0, 0, 0, 0, 0, 0, 0]

for i in command:
    nx, ny = x + dx[i], y + dy[i]

    if not 0 <= nx < n or not 0 <= ny < m:
        continue

    x, y = nx, ny

    if i == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif i == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif i == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    elif i == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]

    if graph[x][y] == 0:
        graph[x][y] = dice[6]
    else:
        dice[6] = graph[x][y]
        graph[x][y] = 0

    print(dice[1])
