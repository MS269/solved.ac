n = int(input())

if n < 100:
    print(n)
else:
    ans = 99
    for i in range(100, min(1000, n + 1)):
        nums = []
        while i > 0:
            nums.append(i % 10)
            i //= 10

        if nums[0] - nums[1] == nums[1] - nums[2]:
            ans += 1

    print(ans)
