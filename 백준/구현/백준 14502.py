import itertools
import sys
import copy
sys.setrecursionlimit(10**6)
N, M = map(int,input().split())


a = [list(map(int,input().split())) for _ in range(N)]
b= copy.deepcopy(a)


plain = []
for i in range(N):
    for j in range(M):
        if a[i][j] == 0:
            plain.append([i,j])

p = itertools.combinations(plain,3)

def dfs(x,y):
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    if(a[x][y] ==2):
        for i in range(4):
            next_x = x +dx[i]
            next_y = y +dy[i]
            if (next_x >=0 and next_y>=0 and next_x<N and next_y<M):
                if(a[next_x][next_y] == 0):                
                    a[next_x][next_y] = 2
                    dfs(next_x,next_y)

result = 0
for i in p:
    count = 0
    x = i[0][0]
    y = i[0][1]
    x1 = i[1][0]
    y1 = i[1][1]
    x2 = i[2][0]
    y2 = i[2][1]
    a[x][y] = 1
    a[x1][y1] = 1
    a[x2][y2] = 1
    for i in range(N):
        for j in range(M):
            dfs(i,j)
    
    for i in range(N):
        for j in range(M):
            if a[i][j] == 0:
                count += 1

    result = max(result,count)
    a = copy.deepcopy(b)
print(result)