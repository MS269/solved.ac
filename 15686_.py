from itertools import combinations
from sys import maxsize


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

houses = []
shops = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append((i, j))
        elif graph[i][j] == 2:
            shops.append((i, j))

ans = maxsize
for open in combinations(shops, m):
    sum_dist = 0
    for house in houses:
        dist = maxsize
        for j in range(m):
            dist = min(dist, abs(house[0] - open[j]
                       [0]) + abs(house[1] - open[j][1]))
        sum_dist += dist
    ans = min(ans, sum_dist)

print(ans)
