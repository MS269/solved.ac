from copy import deepcopy
import sys


input = sys.stdin.readline

n = int(input())
max_cur, max_prev = [0] * 3, [0] * 3
min_cur, min_prev = [0] * 3, [0] * 3

for i in range(n):
    line = list(map(int, input().split()))

    max_cur[0] = max(max_prev[0], max_prev[1]) + line[0]
    max_cur[1] = max(max_prev) + line[1]
    max_cur[2] = max(max_prev[1], max_prev[2]) + line[2]

    min_cur[0] = min(min_prev[0], min_prev[1]) + line[0]
    min_cur[1] = min(min_prev) + line[1]
    min_cur[2] = min(min_prev[1], min_prev[2]) + line[2]

    max_prev = deepcopy(max_cur)
    min_prev = deepcopy(min_cur)

print(max(max_cur), min(min_cur))
