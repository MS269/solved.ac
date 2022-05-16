n = int(input())
graph = [[" "] * (2 * n) for _ in range(n)]


def recursive(x, y, z):
    if z == 3:
        graph[x][y] = "*"
        graph[x + 1][y - 1] = graph[x + 1][y + 1] = "*"
        for i in range(-2, 3):
            graph[x + 2][y + i] = "*"
        return

    nz = z // 2
    recursive(x, y, nz)
    recursive(x + nz, y - nz, nz)
    recursive(x + nz, y + nz, nz)


recursive(0, n - 1, n)

for row in graph:
    print("".join(row))
