from collections import deque


n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def roll(x, y, dx, dy):
    while graph[x + dx][y + dy] != "#" and graph[x][y] != "O":
        x, y = x + dx, y + dy
    return x, y


def bfs(rx, ry, bx, by):
    q = deque([(rx, ry, bx, by, 0)])
    visited = set([(rx, ry, bx, by)])

    while q:
        rx, ry, bx, by, c = q.popleft()

        if c >= 10:
            return -1

        for i in range(4):
            nrx, nry = roll(rx, ry, dx[i], dy[i])
            nbx, nby = roll(bx, by, dx[i], dy[i])

            if graph[nbx][nby] == "O":
                continue
            if graph[nrx][nry] == "O":
                return c + 1

            if nrx == nbx and nry == nby:
                if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                    nrx, nry = nrx - dx[i], nry - dy[i]
                else:
                    nbx, nby = nbx - dx[i], nby - dy[i]

            if (nrx, nry, nbx, nby) not in visited:
                q.append((nrx, nry, nbx, nby, c + 1))
                visited.add((nrx, nry, nbx, nby))

    return -1


for i in range(n):
    for j in range(m):
        if graph[i][j] == "R":
            rx, ry = i, j
        elif graph[i][j] == "B":
            bx, by = i, j

print(bfs(rx, ry, bx, by))
