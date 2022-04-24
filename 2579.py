n = int(input())
a = [0] + [int(input()) for _ in range(n)]

dp = [[0, 0] for _ in range(n + 1)]
dp[1] = [a[1], 0]
if n >= 2:
    dp[2] = [a[1] + a[2], a[2]]
for i in range(3, n + 1):
    dp[i][0] = dp[i - 1][1] + a[i]
    dp[i][1] = max(dp[i - 2]) + a[i]

print(max(dp[n]))
