import sys


input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    line = input().split()

    if line[0] == "push":
        stack.append(int(line[1]))
    elif line[0] == "pop":
        print(stack.pop() if stack else -1)
    elif line[0] == "size":
        print(len(stack))
    elif line[0] == "empty":
        print(1 if not stack else 0)
    elif line[0] == "top":
        print(stack[-1] if stack else -1)
