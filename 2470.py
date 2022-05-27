n = int(input())
a = list(map(int, input().split()))

a.sort()

lo, hi = 0, n - 1
tot = abs(a[0] + a[n - 1])
ans = [a[0], a[n - 1]]

while lo < hi:
    if abs(a[lo] + a[hi]) < tot:
        tot = abs(a[lo] + a[hi])
        ans = [a[lo], a[hi]]

    if a[lo] + a[hi] < 0:
        lo += 1
    else:
        hi -= 1

print(*ans)
