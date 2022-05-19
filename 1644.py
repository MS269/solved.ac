n = int(input())

sieve = [True] * (n + 1)
sieve[0] = sieve[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if not sieve[i]:
        continue

    for j in range(i * i, n + 1, i):
        sieve[j] = False

pnums = [i for i in range(n + 1) if sieve[i]]

ans = 0
tot = 0
lo, hi = 0, 0

while lo < len(pnums):
    if tot == n:
        ans += 1

    if tot >= n or hi == len(pnums):
        tot -= pnums[lo]
        lo += 1
    elif tot < n:
        tot += pnums[hi]
        hi += 1

print(ans)
