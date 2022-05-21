import sys


input = sys.stdin.readline
inf = sys.maxsize


def divnconq(lo, hi):
    if dp[lo][hi] != -1:
        return dp[lo][hi]

    if lo == hi:
        return 0

    ret = inf
    for i in range(lo, hi):
        ret = min(ret, divnconq(lo, i) +
                  divnconq(i + 1, hi) + psum[hi] - psum[lo - 1])
        dp[lo][hi] = ret

    return ret


for _ in range(int(input())):
    k = int(input())
    a = list(map(int, input().split()))
    dp = [[-1] * k for _ in range(k)]

    psum = {-1: 0}
    for i in range(k):
        psum[i] = psum[i - 1] + a[i]

    print(divnconq(0, k - 1))
