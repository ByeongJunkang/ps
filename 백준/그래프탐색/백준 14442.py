from collections import deque
import math
n,m,k = map(int,input().split())
maze = [list(map(int,input())) for _ in range(n)]
ans = math.inf
visited = [[[False]*m for _ in range(n)] for _ in range(k+1)]
dx = [0,1,-1,0]
dy = [1,0,0,-1]
cnt = 0
def bfs(x,y):
    global ans
    q= deque()
    q.append((x,y,0,0))
    visited[0][x][y] = True
    while q:
        cur_x,cur_y,cur_broken,cur_len= q.popleft()
        if cur_x==n-1 and cur_y == m-1:
            ans = min(ans,cur_len)
            break

        for i in range(4):
            next_x, next_y = cur_x + dx[i] , cur_y + dy[i]
            if 0<=next_x < n and 0 <= next_y < m:
                if maze[next_x][next_y] == 0 and not visited[cur_broken][next_x][next_y] :
                    q.append((next_x,next_y,cur_broken,cur_len+1))
                    visited[cur_broken][next_x][next_y] = True
                elif maze[next_x][next_y] == 1 and cur_broken < k and not visited[cur_broken][next_x][next_y] :
                    visited[cur_broken][next_x][next_y] = True
                    q.append((next_x,next_y,cur_broken+1,cur_len+1))

bfs(0,0)
for i in range(k+1):
    for j in range(n):
        for h in range(m):
            print(visited[i][j][h],end=" ")
        print("")
    print("--------------------------------")
if ans == math.inf:
    print(-1)
else:
    print(ans+1)
