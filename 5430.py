from collections import deque


for _ in range(int(input())):
    p = input()
    n = int(input())
    q = deque(input()[1:-1].split(","))

    if n == 0:
        q = deque()

    try:
        is_reversed = False
        for c in p:
            if c == "R":
                is_reversed = not is_reversed
            elif c == "D":
                if is_reversed:
                    q.pop()
                else:
                    q.popleft()

        if is_reversed:
            q.reverse()

        print("[", ",".join(q), "]", sep="")
    except:
        print("error")
