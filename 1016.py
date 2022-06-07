a, b = map(int, input().split())

dp = [1] * (b - a + 1)
for i in range(2, int(b ** 0.5) + 1):
    i = i * i
    for j in range(a // i * i, b + 1, i):
        if j - a >= 0:
            dp[j - a] = 0

print(sum(dp))
