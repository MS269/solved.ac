import heapq


n = int(input())
pq = []
ans = 0

for _ in range(n):
    m = int(input())
    heapq.heappush(pq, m)

while len(pq) > 1:
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)

    ans += a + b
    heapq.heappush(pq, a + b)

print(ans)
