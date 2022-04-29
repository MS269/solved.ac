for _ in range(int(input())):
    x, y = map(int, input().split())

    dist = y - x

    n = 0
    while n * (n + 1) < dist:
        n += 1

    print(2 * n - 1 if dist <= n ** 2 else 2 * n)
