import sys


sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))
dp = [[-1] * (n + 1) for _ in range(n + 1)]


def dfs(lo, hi):
    if dp[lo][hi] != -1:
        return dp[lo][hi]

    if lo >= hi:
        dp[lo][hi] = 1
    elif lo < hi:
        if a[lo] == a[hi]:
            dp[lo][hi] = dfs(lo + 1, hi - 1)
        else:
            dp[lo][hi] = 0

    return dp[lo][hi]


for _ in range(int(input())):
    s, e = map(int, input().split())
    print(dfs(s, e))
