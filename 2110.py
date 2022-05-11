from sys import stdin


input = stdin.readline

n, c = map(int, input().split())
a = [int(input()) for _ in range(n)]


def binary_search(a):
    left, right = 1, a[-1] - a[0]

    while left <= right:
        mid = (left + right) // 2
        cur = a[0]
        cnt = 1

        for i in range(1, len(a)):
            if a[i] - cur >= mid:
                cur = a[i]
                cnt += 1

        if cnt >= c:
            left = mid + 1
        else:
            right = mid - 1

    return right


print(binary_search(sorted(a)))
