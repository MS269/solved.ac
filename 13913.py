from collections import deque


inf = 10 ** 5 + 1

n, k = map(int, input().split())
dist = [-1] * inf
prev = [-1] * inf


def bfs(x):
    q = deque([x])
    dist[x] = 0

    while q:
        x = q.popleft()

        if x == k:
            return dist[k]

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < inf and dist[nx] == -1:
                q.append(nx)
                dist[nx] = dist[x] + 1
                prev[nx] = x


def path(x):
    a = []
    temp = x

    for _ in range(dist[x] + 1):
        a.append(temp)
        temp = prev[temp]

    return a[::-1]


print(bfs(n))
print(*path(k))
