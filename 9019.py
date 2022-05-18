from collections import deque
import sys


input = sys.stdin.readline


def bfs(a, b):
    q = deque([(a, "")])
    visited = set([a])

    while q:
        x, op = q.popleft()

        if x == b:
            return op

        nx = (x * 2) % 10000
        if nx not in visited:
            q.append((nx, op + "D"))
            visited.add(nx)

        nx = (x - 1) % 10000
        if nx not in visited:
            q.append((nx, op + "S"))
            visited.add(nx)

        nx = (x % 1000) * 10 + x // 1000
        if nx not in visited:
            q.append((nx, op + "L"))
            visited.add(nx)

        nx = x // 10 + (x % 10) * 1000
        if nx not in visited:
            q.append((nx, op + "R"))
            visited.add(nx)


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(bfs(a, b))
