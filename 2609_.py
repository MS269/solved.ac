n, m = map(int, input().split())


def gcd(a, b):
    if b > a:
        a, b = b, a

    while b:
        a, b = b, a % b

    return a


def lcd(a, b):
    return a * b // gcd(a, b)


print(gcd(n, m), lcd(n, m))
