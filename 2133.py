n = int(input())

dp = [0] * 31
dp[0] = 1
for i in range(2, n + 1, 2):
    dp[i] = dp[i - 2] * 3 + sum(dp[:i - 2:2]) * 2

print(dp[n])
