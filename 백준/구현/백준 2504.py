# () []은 올바른 괄호열
# (()) ,([]), [[]], [()] 도 올바른 괄호열
# ( ) = 2 [] = 3 (x) = 2 * x , [x] = 3 * x

string = list(input())


stack = []
result = 0
n= 1
for i in range(len(string)):
    if string[i] == '(' :
        n *= 2
        stack.append(string[i])

    elif string[i] == '[' :
        n *= 3
        stack.append(string[i])

    elif string[i] == ')'  :
        if not stack or stack[-1] != '(':
            result = 0
            break
        if string[i-1] == '(':
            result += n
        stack.pop()
        n //= 2
    
    elif string[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if string[i-1] == '[':
            result += n
        stack.pop()
        n //= 3

if stack:
    print(0)
else:
    print(result)