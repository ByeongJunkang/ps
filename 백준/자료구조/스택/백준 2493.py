N = int(input())
top = list(map(int,input().split()))
stack =[]
result = [0] * N
for i in range(N-1,-1,-1): 
    while stack:
        if top[i] > top[stack[-1]]:
            result[stack[-1]] = i + 1 
            stack.pop()
        else:
            break
    stack.append(i)
print(*result)