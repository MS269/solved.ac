s = input()

ans = len(s)
for i in range(len(s) - 1):
    if s[i: i + 2] == "c=":
        ans -= 1
    elif s[i: i + 2] == "c-":
        ans -= 1
    elif s[i: i + 2] == "d-":
        ans -= 1
    elif s[i: i + 2] == "lj":
        ans -= 1
    elif s[i: i + 2] == "nj":
        ans -= 1
    elif s[i: i + 2] == "s=":
        ans -= 1
    elif s[i: i + 2] == "z=":
        if i - 1 >= 0 and s[i - 1] == "d":
            ans -= 1
        ans -= 1

print(ans)
