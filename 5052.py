for _ in range(int(input())):
    n = int(input())
    a = [input() for _ in range(n)]

    a.sort()

    flag = True
    for i in range(n - 1):
        if a[i] == a[i + 1][:len(a[i])]:
            flag = False
            break

    print("YES" if flag else "NO")
