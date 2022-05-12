import sys


sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
m = int(input())
edges = [list(map(int, input().split())) for _ in range(m)]
parent = list(range(n + 1))


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a


def kruskal(edges):
    edges.sort(key=lambda edge: edge[2])
    cost = 0
    for a, b, c in edges:
        if find(a) != find(b):
            union(a, b)
            cost += c
    return cost


print(kruskal(edges))
