import sys


input = sys.stdin.readline

n, m, k = map(int, input().split())
l = [0] + [int(input()) for _ in range(n)]
tree = [0] * (n + 1)


def update(index, diff):
    while index <= n:
        tree[index] += diff
        index += index & -index


def psum(index):
    result = 0
    while index > 0:
        result += tree[index]
        index -= index & -index
    return result


for i in range(1, n + 1):
    update(i, l[i])

for _ in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        diff = c - l[b]
        l[b] = c
        update(b, diff)
    elif a == 2:
        print(psum(c) - psum(b - 1))
