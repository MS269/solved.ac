n = int(input())
a = sorted([list(map(int, input().split())) for _ in range(n)])

for x, y in a:
    print(x, y)
