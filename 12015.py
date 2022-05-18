import bisect


n = int(input())
a = list(map(int, input().split()))
stack = [0]

for i in a:
    if stack[-1] < i:
        stack.append(i)
    else:
        stack[bisect.bisect_left(stack, i)] = i

print(len(stack) - 1)
