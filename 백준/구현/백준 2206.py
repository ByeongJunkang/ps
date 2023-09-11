import math
from collections import deque
n,m = map(int,input().split())
maze = [list(map(int,input())) for _ in range(n)]
visited = [[[False]*m for _ in range(n)] for _ in range(2) ]
q = deque()
q.append((0,0,1,0))
dx = [1,0,-1,0]
dy = [0,1,0,-1]
ans = math.inf
while q:
    cur_x, cur_y, cur_len,cur_break = q.popleft()
    if cur_x == n-1 and cur_y == m-1:
        ans = min(ans,cur_len)
        break
    for i in range(4):
        nx,ny = cur_x + dx[i], cur_y + dy[i]
        if 0 <= nx < n and 0<= ny <m:
            if maze[nx][ny] == 0 and not visited[cur_break][nx][ny]:
                visited[cur_break][nx][ny] = True
                q.append((nx,ny,cur_len+1,cur_break))
            elif maze[nx][ny] == 1 and not visited[cur_break][nx][ny] and cur_break < 1:
                visited[cur_break+1][nx][ny] = True
                q.append((nx,ny,cur_len+1,cur_break+1))

if ans == math.inf:
    print(-1)
else:
    print(ans)