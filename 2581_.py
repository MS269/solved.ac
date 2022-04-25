m = int(input())
n = int(input())

prime_nums = []
for i in range(max(2, m), n + 1):
    flag = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            flag = False
            break

    if flag:
        prime_nums.append(i)

if prime_nums:
    print(sum(prime_nums))
    print(min(prime_nums))
else:
    print(-1)
