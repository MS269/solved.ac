from collections import deque


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)


def bfs(x, y):
    q = deque([(x, y)])
    graph[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = 0
                    cnt += 1

    return cnt


cnts = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnts.append(bfs(i, j))

print(len(cnts))
print(*sorted(cnts), sep="\n")
