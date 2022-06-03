import sys


input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
parents = list(range(n + 1))

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))


def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a


def kruskal():
    edges.sort()
    rslt = 0
    cnt = 0

    for c, a, b in edges:
        if cnt + 2 == n:
            break

        if find(a) != find(b):
            union(a, b)
            rslt += c
            cnt += 1

    return rslt


print(kruskal())
