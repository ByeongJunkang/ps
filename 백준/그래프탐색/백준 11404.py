import math
n = int(input())
m = int(input())
distance = [[math.inf] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    distance[i][i] = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    distance[a][b] = min(distance[a][b],c)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            distance[i][j] = min(distance[i][j],distance[i][k] + distance[k][j])


for i in range(1,n+1):
    for j in range(1,n+1):
        if distance[i][j] == math.inf:
            print(0,end= " ")
        else:
            print(distance[i][j],end= " ")
    print("")