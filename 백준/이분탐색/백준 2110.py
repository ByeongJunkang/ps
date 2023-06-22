import sys
N, C = map(int,input().split())
house = [int(input()) for _ in range(N)]
house.sort()

left, right = 1, house[-1]- house[0]
answer = 0
while left <= right:
    middle = (left+right)//2
    num = house[0]
    count = 1
    for i in range(1,len(house)):
        if house[i] >= num + middle:
            count +=1
            num = house[i]       
    if count >= C:
        left = middle +1
        answer = middle    
    else:
        right = middle - 1
print(answer)
