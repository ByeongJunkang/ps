from collections import deque
M, N = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(N)]
queue = deque()
day = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i,j,day))

def bfs():
    global day
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while queue:
        cur_x , cur_y,cur_day = queue.popleft()
        day = cur_day
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if next_x>=0 and next_x < N and next_y >=0 and next_y <M:
                if box[next_x][next_y] == 0:
                    box[next_x][next_y] =  box[cur_x][cur_y]+1
                    queue.append((next_x,next_y,cur_day+1))

bfs()
a = 0
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    a = max(a, max(i))
print(a- 1)

