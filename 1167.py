v = int(input())
graph = [[] for _ in range(v + 1)]

for _ in range(v):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp) - 2, 2):
        graph[temp[0]].append((temp[i], temp[i + 1]))


def dfs(x):
    for nx, nw in graph[x]:
        if visited[nx] == -1:
            visited[nx] = visited[x] + nw
            dfs(nx)


visited = [-1] * (v + 1)
visited[1] = 0
dfs(1)

x = visited.index(max(visited))
visited = [-1] * (v + 1)
visited[x] = 0
dfs(x)

print(max(visited))
