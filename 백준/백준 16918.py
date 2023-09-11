r,c,n= map(int,input().split())
bomb = [list(input()) for _ in range(r)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def bfs(x,y):
    if bomb[x][y] == "O":
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < r and 0<= next_y < c and bomb[next_x][next_y] != "O":
                bomb[next_x][next_y] = "."
        bomb[x][y] = "."
    return


def bfs1(x,y):
    if bomb[x][y] == "X":
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < r and 0<= next_y < c and bomb[next_x][next_y] != "X":
                bomb[next_x][next_y] = "."

        bomb[x][y] = "."
    return

flag = 0
for time in range(2,n+1):
    if time % 2 == 0:
        for i in range(r):
            for j in range(c):
                if bomb[i][j] == "." and flag == 0:
                    bomb[i][j] = "X"
                elif bomb[i][j] == "." and flag == 1:
                    bomb[i][j] = "O"
    
    elif time % 2 == 1:
        for i in range(r):
            for j in range(c):
                if flag == 0:
                    bfs(i,j)
                    
                elif flag == 1:
                    bfs1(i,j)

        if flag ==1:
            flag = 0
        else:
            flag = 1

for i in range(r):
    for j in range(c):
        if bomb[i][j] == "X":
            print("O", end = "")
        else:
            print(bomb[i][j],end="")
    print()