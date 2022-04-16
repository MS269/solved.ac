remove_set = set()
for i in range(1, 10001):
    d = i
    while i > 0:
        d += i % 10
        i //= 10

    remove_set.add(d)

self_nums = sorted(set(range(1, 10001)) - remove_set)
print(*self_nums, sep="\n")
