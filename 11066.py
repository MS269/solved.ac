import sys


input = sys.stdin.readline
inf = sys.maxsize

for _ in range(int(input())):
    k = int(input())
    a = list(map(int, input().split()))
    dp = [[0] * k for _ in range(k)]

    psum = {-1: 0}
    for i in range(k):
        psum[i] = psum[i - 1] + a[i]

    for i in range(1, k):
        for lo in range(k - 1):
            hi = lo + i

            if hi >= k:
                break

            rslt = inf
            for mid in range(lo, hi):
                rslt = min(rslt, dp[lo][mid] + dp[mid + 1]
                           [hi] + psum[hi] - psum[lo - 1])

            dp[lo][hi] = rslt

    print(dp[0][-1])
