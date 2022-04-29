n = int(input())

column = [0] * n
ans = 0


def bt(x):
    global ans

    if x == n:
        ans += 1
        return

    for i in range(n):
        column[x] = i

        flag = True
        for j in range(x):
            if column[j] == column[x] or abs(j - x) == abs(column[j] - column[x]):
                flag = False
                break

        if flag:
            bt(x + 1)


bt(0)

print(ans)
