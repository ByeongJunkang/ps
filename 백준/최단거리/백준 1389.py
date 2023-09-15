import math
n,m = map(int,input().split())
dis = [[math.inf] * (n+1) for _ in range(n + 1)]

for _ in range(m):
    a,b = map(int,input().split())
    dis[b][a] = 1
    dis[a][b] =1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dis[i][j] = min(dis[i][j],dis[k][j] + dis[i][k])


tmp_sum = 10**9
for i in range(1,n+1):
    tmp = 0
    for j in range(1,n+1):
        if i!=j:
            tmp+=dis[i][j]
    
    if tmp_sum > tmp:
        tmp_sum = tmp
        ans = i


print(ans)
    