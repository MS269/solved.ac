n = int(input())
m = int(input())
broken = set(input().split()) if m else set()

ans = abs(n - 100)
for i in range(1000001):
    num = str(i)

    for digit in num:
        if digit in broken:
            break
    else:
        ans = min(ans, len(num) + abs(n - i))

print(ans)
