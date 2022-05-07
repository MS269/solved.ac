import sys


sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = list(range(n + 1))


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for _ in range(m):
    a, b, c = map(int, input().split())

    if a == 0:
        union(b, c)
    else:
        print("YES" if find(b) == find(c) else "NO")
