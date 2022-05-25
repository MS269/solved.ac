import heapq


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
pq = []
ans = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

while pq:
    x = heapq.heappop(pq)
    ans.append(x)

    for nx in graph[x]:
        indegree[nx] -= 1

        if indegree[nx] == 0:
            heapq.heappush(pq, nx)

print(*ans)
