from collections import deque

N, M = map(int,input().split())

miro = []
for i in range(N):
    miro.append(list(map(int,input())))
visited = [[False] * M for _ in range(N)]




queue = deque()
shortest_length = 0
def bfs(x,y):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    global shortest_length
    queue.append((x,y,shortest_length))
    while queue:
        cur_x , cur_y, cur_len = queue.popleft()
        if cur_x == N -1 and cur_y == M-1:
            shortest_length = cur_len
            break
        for i in range(4):
            next_x = cur_x+dx[i]
            next_y = cur_y+dy[i]
            if(miro[x][y]==1):
                if(next_x>=0 and next_y>=0 and next_x<N and next_y<M):
                    if (miro[next_x][next_y] == 1 and not visited[next_x][next_y]):
                        queue.append((next_x,next_y,cur_len+1))
                        visited[next_x][next_y] = True

    return shortest_length       


for i in range(N ):
    for j in range(M):
        bfs(i,j)

print(shortest_length + 1)