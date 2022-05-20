s = input()
stack = []
ans = []

for c in s:
    if c.isalpha():
        ans += c
    elif c == "(":
        stack.append(c)
    elif c == ")":
        while stack and stack[-1] != "(":
            ans += stack.pop()
        stack.pop()
    elif c == "*" or c == "/":
        while stack and (stack[-1] == "*" or stack[-1] == "/"):
            ans += stack.pop()
        stack.append(c)
    elif c == "+" or c == "-":
        while stack and stack[-1] != "(":
            ans += stack.pop()
        stack.append(c)

while stack:
    ans += stack.pop()

print("".join(ans))
