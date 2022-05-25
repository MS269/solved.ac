n = int(input())
parents = list(map(int, input().split()))
remove = int(input())


def dfs(x):
    parents[x] = -2

    for i in range(n):
        if parents[i] == x:
            dfs(i)


dfs(remove)

ans = 0
for i in range(n):
    if parents[i] != -2 and i not in parents:
        ans += 1

print(ans)
