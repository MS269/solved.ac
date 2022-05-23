n = int(input())
a = list(map(int, input().split()))

dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_len = max(dp)
subseq = []

i, j = n - 1, max_len
while i >= 0 and j > 0:
    if dp[i] == j:
        subseq.append(a[i])
        j -= 1
    i -= 1

print(max_len)
print(*subseq[::-1])
