import sys
board = [list(map(int,input().split())) for _ in range(19)]
dx = [1,1,0,-1]
dy =[0,1,1,1]

def dfs(x,y,cnt,dir,ox,oy):
    if cnt == 5:
        if 0 <= x + dx[dir] < 19 and 0 <=y + dy[dir] < 19:
            if board[x+dx[dir]][y+dy[dir]] == board[ox][oy]:
                return
        
        if 0 <= ox - dx[dir] < 19 and 0 <=oy - dy[dir] < 19:
            if board[ox-dx[dir]][oy -dy[dir]] == board[ox][oy]:
                return

        print(board[x][y])
        print(ox+1,oy+1)
        sys.exit()
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < 19 and 0 <=ny < 19:
        if board[nx][ny] == board[x][y]:
            dfs(nx,ny,cnt+1,dir,ox,oy)    

for i in range(19):
    for j in range(19):
        if board[i][j] !=0:
            for dir in range(4):
                dfs(i,j,1,dir,i,j)
                    
print(0)