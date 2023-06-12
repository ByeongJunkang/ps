N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
blue = 0
white = 0
def bfs(i,j,N):
    global blue,white
    color = paper[i][j]
    for a in range(i,i+N):
        for b in range(j,j+N):
            if color != paper[a][b]:
                bfs(i,j,N//2)
                bfs(i, j+N//2,N//2)
                bfs(i+N//2,j,N//2)
                bfs(i+N//2,j+N//2,N//2)
                return

    if color == 0:
        white+=1
    else:
        blue +=1

bfs(0,0,N)
print(white)
print(blue)