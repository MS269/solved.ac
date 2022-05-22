import sys


input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [[0] * n for _ in range(n)]

for i in range(n):
    for lo in range(n):
        hi = lo + i

        if hi >= n:
            break

        if lo == hi:
            dp[lo][hi] = 1
            continue

        if lo + 1 == hi and a[lo] == a[hi]:
            dp[lo][hi] = 1
            continue

        if a[lo] == a[hi] and dp[lo + 1][hi - 1]:
            dp[lo][hi] = 1

for _ in range(int(input())):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])
