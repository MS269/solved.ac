n = int(input())
k = int(input())


def bisect(lo, hi):
    while lo <= hi:
        mid = (lo + hi) // 2
        cnt = 0

        for i in range(1, n + 1):
            cnt += min(mid // i, n)

        if cnt < k:
            lo = mid + 1
        else:
            hi = mid - 1

    return lo


print(bisect(1, n * n))
