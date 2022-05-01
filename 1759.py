from itertools import combinations


l, c = map(int, input().split())
a = sorted(input().split())

vowels = set(("a", "e", "i", "o", "u"))

for word in combinations(a, l):
    vowel_cnt = 0
    consonant_cnt = 0

    for char in word:
        if char in vowels:
            vowel_cnt += 1
        else:
            consonant_cnt += 1

    if vowel_cnt >= 1 and consonant_cnt >= 2:
        print("".join(word))
