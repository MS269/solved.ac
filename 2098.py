import sys


inf = sys.maxsize

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[inf] * (1 << n) for _ in range(n)]


def dfs(x, visited):
    if visited == (1 << n) - 1:
        if graph[x][0]:
            return graph[x][0]
        return inf

    if dp[x][visited] != inf:
        return dp[x][visited]

    for i in range(1, n):
        if graph[x][i] == 0:
            continue
        if visited & (1 << i):
            continue

        dp[x][visited] = min(dp[x][visited], dfs(
            i, visited | (1 << i)) + graph[x][i])

    return dp[x][visited]


print(dfs(0, 1))
