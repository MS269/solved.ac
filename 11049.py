import sys


input = sys.stdin.readline
inf = sys.maxsize

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for size in range(1, n):
    for lo in range(n - size):
        hi = lo + size
        dp[lo][hi] = inf

        for mid in range(lo, hi):
            dp[lo][hi] = min(dp[lo][hi], dp[lo][mid] + dp[mid + 1]
                             [hi] + a[lo][0] * a[mid][1] * a[hi][1])

print(dp[0][n - 1])
