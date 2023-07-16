N = int(input())
num = sorted(list(map(int,input().split())))
x = int(input())
left = 0
right =N-1
answer=  0
while left <right:
    if num[left] + num[right] == x:
        left+=1
        right-=1
        answer +=1
    
    elif num[left] + num[right] < x:
        left +=1
    
    else:
        right -=1

print(answer)
