from math import gcd


n, m = map(int, input().split())

print(gcd(n, m), n * m // gcd(n, m))
