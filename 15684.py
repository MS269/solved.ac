import sys


input = sys.stdin.readline

n, m, h = map(int, input().split())
visited = [[False] * n for _ in range(h)]
ans = 4


def check():
    for k in range(n):
        j = k

        for i in range(h):
            if visited[i][j]:
                j += 1
            elif j > 0 and visited[i][j - 1]:
                j -= 1

        if j != k:
            return False

    return True


def dfs(x, y, c):
    global ans

    if check():
        ans = min(ans, c)
        return

    if c == 3 or c >= ans:
        return

    for i in range(x, h):
        if i == x:
            k = y
        else:
            k = 0

        for j in range(k, n - 1):
            if visited[i][j] or visited[i][j + 1]:
                continue
            if j > 0 and visited[i][j - 1]:
                continue

            visited[i][j] = True
            dfs(i, j + 2, c + 1)
            visited[i][j] = False


if m == 0:
    print(0)
    sys.exit()

for _ in range(m):
    a, b = map(int, input().split())
    visited[a - 1][b - 1] = True

dfs(0, 0, 0)

print(ans if ans < 4 else -1)
