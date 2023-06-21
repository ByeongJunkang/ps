K, N = map(int,input().split())
cable = []
for _ in range(K):
    cable.append(int(input()))

answer = []
left,right = 1, max(cable)
while left <= right:
    middle = (left+right) //2
    
    num = 0
    for i in cable:
        num += i//middle

    if num >=N:
        left = middle+1
        answer.append(middle)
    elif num <N:
        right = middle-1
    

print(max(answer))