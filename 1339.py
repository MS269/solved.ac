n = int(input())
a = [input() for _ in range(n)]
alphabets = [0] * 26

for i in range(n):
    for j in range(len(a[i])):
        alphabets[ord(a[i][j]) - 65] += 10 ** (len(a[i]) - j - 1)

ans = 0

for i in range(9, -1, -1):
    max_idx = 0

    for j in range(26):
        if alphabets[j] > alphabets[max_idx]:
            max_idx = j

    if alphabets[max_idx] == 0:
        break

    ans += alphabets[max_idx] * i
    alphabets[max_idx] = 0

print(ans)
