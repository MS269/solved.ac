import sys


n, s = map(int, input().split())
a = list(map(int, input().split()))

sub = [0] * (n + 1)
for i in range(1, n + 1):
    sub[i] = sub[i - 1] + a[i - 1]

ans = sys.maxsize
left = 0
right = 1

while left != n:
    if sub[right] - sub[left] >= s:
        ans = min(ans, right - left)
        left += 1
    elif right != n:
        right += 1
    else:
        left += 1

print(ans if ans != sys.maxsize else 0)
