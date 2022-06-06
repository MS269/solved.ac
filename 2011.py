a = [0] + list(map(int, input()))
dp = [0] * len(a)

if a[1] == 0:
    print(0)
else:
    dp[0] = dp[1] = 1
    for i in range(2, len(a)):
        if a[i] > 0:
            dp[i] += dp[i - 1]
        if 10 <= a[i - 1] * 10 + a[i] <= 26:
            dp[i] += dp[i - 2]
        dp[i] %= 10 ** 6

    print(dp[-1])
