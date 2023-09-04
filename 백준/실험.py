from collections import deque

def solution(maps):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    start_x,start_y = 0,0
    for i in range(len(maps)):
        for j in range(len(maps)):
            if maps[i][j] == "S":
                start_x,start_y = i,j
    N = len(maps)
    visited = [[False] * N for _ in range(N)]
    q = deque()
    q.append((start_x,start_y,0))
    visited[start_x][start_y] = True
    is_lebber_on = False
    while q:
        cur_x,cur_y,cur_len = q.popleft()
        if not is_lebber_on and maps[next_x][next_y] == 'L':
            visited = [[False]*N for _ in range(N)]
            visited[next_x][next_y] = True
            q = deque()
            q.append((next_x,next_y,cur_len+1))
            is_lebber_on = True
            continue
        
        if maps[cur_x][cur_y] == 'E' and is_lebber_on == True:
            return cur_len
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N:
                if maps[next_x][next_y] != 'X' and not visited[next_x][next_y]:
                    q.append((next_x,next_y,cur_len +1))
                    visited[next_x][next_y] = True
               
            
            
            
        return -1