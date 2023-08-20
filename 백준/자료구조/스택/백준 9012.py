N = int(input())
for _ in range(N):
    symbol = list(input())
    stack = []
    for letter in symbol:
        if letter == '(':
            stack.append(letter)
        elif letter == ')' and len(stack) > 0:
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(letter)

        else:
            break
    if len(stack) > 0:
        print("NO")
    else:
        print("YES")
