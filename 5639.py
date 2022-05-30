import sys


sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

preorder = []

while True:
    try:
        preorder.append(int(input()))
    except:
        break


def postorder(lo, hi):
    if lo > hi:
        return

    mid = hi + 1

    for i in range(lo + 1, hi + 1):
        if preorder[i] > preorder[lo]:
            mid = i
            break

    postorder(lo + 1, mid - 1)
    postorder(mid, hi)
    print(preorder[lo])


postorder(0, len(preorder) - 1)
