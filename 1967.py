import sys


sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dfs(x):
    for nx, w in graph[x]:
        if visited[nx] == -1:
            visited[nx] = visited[x] + w
            dfs(nx)


visited = [-1] * (n + 1)
visited[1] = 0
dfs(1)

x = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[x] = 0
dfs(x)

print(max(visited))
