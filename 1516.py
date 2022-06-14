from collections import deque
import sys


input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)
ans = [0] * (n + 1)

for i in range(1, n + 1):
    line = list(map(int, input().split()))

    time[i] = line[0]
    prebuild = line[1:-1]

    for j in prebuild:
        graph[j].append(i)
        indegree[i] += 1


def topology_sort():
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        x = q.popleft()
        ans[x] += time[x]

        for nx in graph[x]:
            indegree[nx] -= 1
            ans[nx] = max(ans[nx], ans[x])

            if indegree[nx] == 0:
                q.append(nx)


topology_sort()

print(*ans[1:], sep="\n")
