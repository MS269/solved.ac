import sys


graph = [list(map(int, input().split())) for _ in range(9)]
row = [[False] * 10 for _ in range(9)]
column = [[False] * 10 for _ in range(9)]
square = [[False] * 10 for _ in range(9)]

empty = []
for i in range(9):
    for j in range(9):
        n = graph[i][j]
        if n == 0:
            empty.append((i, j))
            continue

        row[i][n] = True
        column[j][n] = True
        square[i // 3 * 3 + j // 3][n] = True


def dfs(c):
    if c == len(empty):
        for i in graph:
            print(*i)
        sys.exit()

    x, y = empty[c]
    s = x // 3 * 3 + y // 3
    for n in range(1, 10):
        if not row[x][n] and not column[y][n] and not square[s][n]:
            graph[x][y] = n
            row[x][n] = True
            column[y][n] = True
            square[s][n] = True
            dfs(c + 1)
            graph[x][y] = 0
            row[x][n] = False
            column[y][n] = False
            square[s][n] = False


dfs(0)
