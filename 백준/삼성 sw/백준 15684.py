n,m,h = map(int,input().split())
board = [[0] * (n) for _ in range(h)]
for _ in range(m):
    a,b = map(int,input().split())
    board[a-1][b-1] = 1
    
def check(board):
    for i in range(n):
        target = i
        j = 0
        for j in range(h):
            if board[j][target]:
                target = target + 1
            elif board[j][target-1] and target >0:
                target -= 1

        if target != i:
            return False
    return True

      
ans = 4
def renew(board,cnt,idx,idx1):
    global ans
    if cnt > 3:
        return
    
    if check(board):
        ans = min(ans,cnt)
        return
    

    for i in range(idx,h):
        if i == idx:
            now = idx1
        else:
            now = 0
        for j in range(now,n-1):
            if board[i][j] == 0 and board[i][j+1] == 0:
                if j >0 and board[i][j-1]:
                    continue
                board[i][j] = 1
                renew(board,cnt+1,i,j+2)
                board[i][j] = 0
              
    
renew(board,0,0,0)
if ans == 4:
    print(-1)
else:
    print(ans)
