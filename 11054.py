n = int(input())
a = list(map(int, input().split()))

asc_dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            asc_dp[i] = max(asc_dp[i], asc_dp[j] + 1)

a.reverse()
desc_dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            desc_dp[i] = max(desc_dp[i], desc_dp[j] + 1)
desc_dp.reverse()

bionic_dp = [asc_dp[i] + desc_dp[i] - 1 for i in range(n)]

print(max(bionic_dp))
