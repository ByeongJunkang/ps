N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
answer = [0]*3
first_color = 0
second_color = 0
third_color = 0
def bfs(x,y,n):
    global first_color
    global second_color
    global third_color
    size = n//3
    if n <1:
        return
    isTrue = True
    norm = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j] != norm:
                isTrue = False
                break
    if isTrue == True:
        if norm == -1:
            first_color +=1
        elif norm == 0:
            second_color +=1
        elif norm == 1:
            third_color +=1
    else:
        bfs(x,y,size) # 이동 x
        bfs(x+size,y,size) # 아래로 3 이동
        bfs(x,y+size,size) # 오른쪽으로 3이동
        bfs(x,y+size*2,size) # 오른쪽으로 6이동
        bfs(x+size*2,y,size) # 아래로 6이동
        bfs(x+size*2, y+size*2,size) #아래로, 오른쪽으로 6이동
        bfs(x+size,y+size*2,size)
        bfs(x+size*2,y+size,size)
        bfs(x+size,y+size,size)

bfs(0,0,N)
print(first_color)
print(second_color)
print(third_color)