#N일 동안 돈을씀
# M번만 인출함
# K원을 인출함
# M번만 인출
#모자라면 남은 금액 통장에 넣고 K원 인출
# 남은 금액이 사용할 금액보다 많더라도
# 통장에 넣고 K원 다시 인출
n,m = map(int,input().split())

import sys
money = []
for _ in range(n):
    a= int(sys.stdin.readline())
    money.append(a)

left = min(money)
right = sum(money)
ans = 0
while left <= right:
    cnt = 0
    total = 0
    mid = (left+right) // 2
    for i in range(n):
        if total < money[i]:
            total = mid
            cnt +=1  
        total -= money[i]
        

    if cnt > m or mid < max(money):
        left= mid + 1 
    
    else:
        right = mid -1
        ans = mid
        
print(ans)
        

        
