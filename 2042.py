import sys


input = sys.stdin.readline

n, m, k = map(int, input().split())
l = [0] + [int(input()) for _ in range(n)]
tree = [0] * (n * 4)


def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)
    return tree[node]


def psum(node, start, end, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return psum(node * 2, start, mid, left, right) + psum(node * 2 + 1, mid + 1, end, left, right)


def update(node, start, end, index, diff):
    if not start <= index <= end:
        return

    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)


init(1, 1, n)

for _ in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        diff = c - l[b]
        l[b] = c
        update(1, 1, n, b, diff)
    elif a == 2:
        print(psum(1, 1, n, b, c))
