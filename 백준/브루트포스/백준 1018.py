n,m= map(int,input().split())
p1 = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
p2 = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
board = [list(input()) for _ in range(n)]
ans = 65
def bfs(x,y):
    global ans
    tmp = 0
    for i in range(8):
        if (i+1)% 2 ==0:
            for j in range(8):
                if board[x+i][y+j] != p1[j]:
                    tmp +=1
        else:
            for j in range(8):
                if board[x+i][y+j] != p2[j]:
                    tmp+=1
    ans = min(ans,tmp,64-tmp) 

for i in range(0,n-7):
    for j in range(0,m-7):
        bfs(i,j)
print(ans)