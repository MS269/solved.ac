n = int(input())
a = [input() for _ in range(n)]

b = list(set(a))

b.sort(key=lambda x: (len(x), x))

print(*b, sep="\n")
