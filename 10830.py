n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


def mul(a, b):
    c = [[0] * len(a) for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(a)):
            temp = 0
            for k in range(len(a)):
                temp += a[i][k] * b[k][j]
            c[i][j] = temp % 1000

    return c


def pow(a, b):
    if b == 1:
        for x in range(n):
            for y in range(n):
                a[x][y] %= 1000
        return a

    half = pow(a, b // 2)
    if b % 2 == 1:
        return mul(mul(half, half), a)
    else:
        return mul(half, half)


result = pow(a, b)

for r in result:
    print(*r)
