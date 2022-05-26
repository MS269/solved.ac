n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = graph[i][j]
        elif graph[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

print(max(list(map(max, dp))) ** 2)
