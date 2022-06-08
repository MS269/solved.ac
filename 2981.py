n = int(input())
a = [int(input()) for _ in range(n)]


def get_gcd(a, b):
    if a < b:
        a, b = b, a

    while b > 0:
        a, b = b, a % b

    return a


b = [abs(a[i + 1] - a[i]) for i in range(n - 1)]

gcd = b[0]
for i in range(1, n - 1):
    gcd = get_gcd(gcd, b[i])

ans = [gcd]
for i in range(2, int(gcd ** 0.5) + 1):
    if gcd % i == 0:
        ans.append(i)
        ans.append(gcd // i)

ans = list(set(ans))

ans.sort()

print(*ans)
