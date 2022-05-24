s = input()
bomb = input()

stack = []
for c in s:
    stack.append(c)

    if c == bomb[-1] and "".join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

print("".join(stack) if stack else "FRULA")
