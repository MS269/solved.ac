n = int(input())

dp = [[0, 0, 0] for _ in range(n + 1)]
for i in range(1, n + 1):
    r, g, b = map(int, input().split())

    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + r
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + g
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + b

print(min(dp[n]))
