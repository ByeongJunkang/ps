import sys,math
N,H = map(int,input().split())
obstacles = [int(sys.stdin.readline()) for _ in range(N)]
upper = []
lower = []
for i,v in enumerate(obstacles):
    if i %2 == 0:
        upper.append(v)
    else:
        lower.append(v)

upper.sort()
lower.sort()
answer = math.inf
num = 1
def check(height,cave):
    left,right = 0,len(cave) - 1
    while left <=right:
        mid = (left + right ) // 2
        if cave[mid] <= height:
            left = mid + 1
        else:
            right = mid - 1
    return len(cave ) - (right + 1) 

for i in range(1,H+1):
    l_cnt = check(i-1,upper)
    h_cnt = check(H-i,lower)
    temp = l_cnt + h_cnt
    if temp < answer:
        answer = temp
        num = 1
    elif temp == answer:
        num+=1    
        
print(answer, num)   

