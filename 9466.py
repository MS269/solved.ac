import sys


sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(x):
    visited[x] = True
    cycle.append(x)

    nx = graph[x]
    if not visited[nx]:
        dfs(nx)
    elif nx in cycle:
        result.extend(cycle[cycle.index(nx):])


for _ in range(int(input())):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    result = []

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(result))
