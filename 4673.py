self_nums = [True] * 10001
for i in range(1, 10001):
    if not self_nums[i]:
        continue

    print(i)

    now = i
    while True:
        next = now
        while now > 0:
            next += now % 10
            now //= 10

        if next > 10000:
            break

        self_nums[next] = False
        now = next
