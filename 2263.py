import sys


sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
pos = [0] * (n + 1)


def preorder(in_lo, in_hi, post_lo, post_hi):
    if in_lo > in_hi or post_lo > post_hi:
        return

    parent = postorder[post_hi]
    print(parent, end=" ")

    left = pos[parent] - in_lo
    right = in_hi - pos[parent]

    preorder(in_lo, in_lo + left - 1, post_lo, post_lo + left - 1)
    preorder(in_hi - right + 1, in_hi, post_hi - right, post_hi - 1)


for i in range(n):
    pos[inorder[i]] = i

preorder(0, n - 1, 0, n - 1)
