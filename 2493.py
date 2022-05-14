n = int(input())
a = list(map(int, input().split()))

ans = [0] * n
stack = []
for i in range(n - 1, -1, -1):
    while stack and a[stack[-1]] <= a[i]:
        ans[stack.pop()] = i + 1
    stack.append(i)

print(*ans)
