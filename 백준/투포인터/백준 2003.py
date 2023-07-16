N, M = map(int,input().split())

num = list(map(int,input().split()))
sum = num[0]
start = 0
end = 1
answer = 0
while end < N:
    if sum < M:
         
        sum += num[end]
        end +=1
   
    
    elif sum > M:
        sum -= num[start]
        start +=1
    elif sum == M:
        answer+=1
        sum -=num[start]
        start +=1
print(answer)
    