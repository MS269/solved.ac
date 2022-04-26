from collections import deque
import sys


input = sys.stdin.readline

n = int(input())

q = deque()
for _ in range(n):
    line = input().split()

    if line[0] == "push":
        q.append(int(line[1]))
    elif line[0] == "pop":
        print(q.popleft() if q else -1)
    elif line[0] == "size":
        print(len(q))
    elif line[0] == "empty":
        print(1 if not q else 0)
    elif line[0] == "front":
        print(q[0] if q else -1)
    elif line[0] == "back":
        print(q[-1] if q else -1)
