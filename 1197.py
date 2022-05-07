v, e = map(int, input().split())
edges = []
parent = list(range(v + 1))

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])


def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


ans = 0
for a, b, w in edges:
    if find(a) != find(b):
        union(a, b)
        ans += w

print(ans)
