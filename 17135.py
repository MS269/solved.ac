from copy import deepcopy
from itertools import combinations


n, m, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
items = list(range(m))
ans = 0


def is_empty():
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 1:
                return False
    return True


def attack(archers):
    attacked = []
    result = 0

    for y in archers:
        candidates = []

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 1:
                    dist = abs(i - n) + abs(j - y)
                    if dist <= d:
                        candidates.append((dist, i, j))

        candidates.sort(key=lambda x: (x[0], x[2]))

        if candidates:
            attacked.append(candidates[0])

    for _, i, j in attacked:
        if temp[i][j] == 1:
            temp[i][j] = 0
            result += 1

    return result


def move():
    for i in range(-1, -n, -1):
        temp[i] = temp[i - 1]
    temp[0] = [0] * m


for archers in combinations(items, 3):
    temp = deepcopy(graph)
    attacked = 0

    while not is_empty():
        attacked += attack(archers)
        move()

    ans = max(ans, attacked)

print(ans)
