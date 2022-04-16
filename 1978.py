n = int(input())
a = list(map(int, input().split()))

prime_nums = [1] * 1001
prime_nums[1] = 0
for i in range(2, 1001):
    if prime_nums[i]:
        for j in range(i + i, 1001, i):
            prime_nums[j] = 0

ans = 0
for i in a:
    ans += prime_nums[i]

print(ans)
