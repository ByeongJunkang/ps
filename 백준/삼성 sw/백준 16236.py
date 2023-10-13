# 상어는 자기보다 큰 물고기 있는 칸은 못지나감
# 자신의 크기보다 작은 물고기만 먹기 가능
# 크기가 같은 물고기는 먹을 수 없고 지나가기 가능

# 물고기가 공간에 없다면, 엄마 상어에게 도움 요청
# 1마리면 그 물고기 먹기
# 먹을 수 있는 고기가 1개 이상 -> 가장 가까움
# 가장 가까운게 여러개? -> 가장 위, 가장 왼쪽

# 상어의 이동은 1초, 물고기 먹는데 걸리는 시간 x
# 물고기를 먹으면 그 칸은 빈칸

# 물고기 먹을 때 마다 크기가 1 증가
# 몇초 동안 엄마상어 도움 없이 

# 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 증가한다.

from collections import deque

n = int(input())
space = [list(map(int,input().split())) for _ in range(n)]
sx,sy = 0,0
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
                sx,sy = i,j            

            
q = deque()
q.append((sx,sy,0,0))
dx = [1,0,-1,0]
dy = [0,1,0,-1] 
shark_size = 2
while q:
    cur_x,cur_y,eat_fish,time = q.popleft()
    space[cur_x][cur_y] = 0
    if eat_fish == shark_size:
        shark_size +=1
        eat_fish = 0

    result = []
    tq = deque()
    tq.append((cur_x,cur_y,0))
    visited = [[False] * n  for _ in range(n)]

    visited[cur_x][cur_y] = True
    while tq:
        cx,cy,cnt = tq.popleft()
        if space[cx][cy] !=0 and space[cx][cy] !=9 and space[cx][cy] < shark_size:
            result.append((cx,cy,cnt))
        for i in range(4):
            next_x,next_y = cx + dx[i], cy + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n:
                if not visited[next_x][next_y]:
                    if space[next_x][next_y] <= shark_size:
                        tq.append((next_x,next_y,cnt+1))
                        visited[next_x][next_y] = True
            

    min_distance = float('inf')
    tmp_result = []
    for i in result:
        nx,ny = i[0],i[1]
        cur_distance = i[2]
        if cur_distance < min_distance:
            tmp_result = [(nx,ny)]
            min_distance = cur_distance
        elif cur_distance == min_distance:
            tmp_result.append((nx,ny))
    
    tmp_result.sort(key= lambda x: (x[0],x[1]))
    if len(tmp_result) > 0:
        rx,ry = tmp_result[0][0],tmp_result[0][1]
        q.append((rx,ry,eat_fish+1,time+min_distance))
        space[rx][ry] = 0
        
    else:
        print(time)
        break




