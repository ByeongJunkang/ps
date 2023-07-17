import math
n,s = map(int,input().split())
num = list(map(int,input().split()))
start = 0
end = 0
length = math.inf
sum = num[0]
while end < n and start < n:
    if sum <s:
        end +=1
        if end < n:
            sum += num[end]
    
    elif sum == s:
        length = min(length,abs(end-start)+1)
        sum -=num[start]
        start +=1
    else:
        length = min(length,abs(end-start)+1)
        sum -=num[start]
        start +=1
    
    if sum == s:
        length = min(length,abs(end-start+1))

if length == math.inf:
    print(0)
else:
    print(length)
