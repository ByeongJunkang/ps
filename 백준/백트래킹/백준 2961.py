import math
N= int(input())
ingr =[]
for _ in range(N):
    ingr.append(list(map(int,input().split())))

min_num = math.inf
def dfs(count,num,sour,bit,target):
    global min_num
    if count == target:
        temp = abs(sour-bit)
        min_num = min(min_num,temp)

    for i in range(num,N):
        dfs(count+1,i+1,sour * ingr[i][0],bit + ingr[i][1],target) 


for i in range(1,N+1):
    dfs(0,0,1,0,i)

print(min_num)