from collections import deque
N,M = map(int,input().split())

aqua = []
for _ in range(N):
    aqua.append(list(map(int,input().split())))

result = 0

def dfs(x,y):

    visited = [[False] * M for _ in range(N)]
    q = deque()
    dx = [1,0,-1,0,-1,-1,1,1]
    dy = [0,-1,0,1,-1,1,-1,1]
    cur_len = 0
    q.append((x,y,cur_len))
    visited[x][y] = True
    min_list = 999999999
    while q:
        cur_x, cur_y,len = q.popleft()
        if aqua[cur_x][cur_y] == 1:
            min_list = min(min_list,len)
        for i in range(8):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if next_x >=0 and next_y >=0 and next_x < N and next_y <M:
                if not visited[next_x][next_y]:
                    q.append((next_x,next_y,len+1))
                    visited[next_x][next_y] = True

    return (min_list)


for i in range(N):
    for j in range(M):
        if aqua[i][j] == 0:
            result = max(result,dfs(i,j))


print(result)