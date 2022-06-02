import heapq
import sys


input = sys.stdin.readline

n, k = map(int, input().split())
gems = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

gems.sort()
bags.sort()

pq = []
ans = 0

for bag in bags:
    while gems and bag >= gems[0][0]:
        heapq.heappush(pq, -gems[0][1])
        heapq.heappop(gems)

    if pq:
        ans += -heapq.heappop(pq)
    elif not gems:
        break

print(ans)
