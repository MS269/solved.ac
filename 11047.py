n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

ans = 0
for coin in reversed(a):
    ans += k // coin
    k %= coin

print(ans)
