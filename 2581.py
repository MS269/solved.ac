m = int(input())
n = int(input())

prime_nums = [False, False] + [True] * (n - 1)
for i in range(2, int(n ** 0.5) + 1):
    if prime_nums[i]:
        for j in range(i * i, n + 1, i):
            prime_nums[j] = False

total = 0
min_value = 0
for i in range(m, n + 1):
    if prime_nums[i]:
        total += i

        if min_value == 0:
            min_value = i

if total:
    print(total)
    print(min_value)
else:
    print(-1)
