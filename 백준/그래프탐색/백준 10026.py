from collections import deque
N = int(input())
pic = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def bfs(x,y,color):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        cur_x,cur_y = q.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if next_x < N and next_x>=0 and next_y < N and next_y >=0:
                if not visited[next_x][next_y] and pic[next_x][next_y] == color:
                    q.append((next_x,next_y))
                    visited[next_x][next_y] = True

ans = 0
for i in range(N):
    for j in range(N):
        if pic[i][j] == "R" and not visited[i][j]:
            bfs(i,j,"R")
            ans +=1
        elif pic[i][j] == "B" and not visited[i][j]:
            bfs(i,j,"B")
            ans +=1
        elif pic[i][j] == "G" and not visited[i][j]:
            bfs(i,j,"G")
            ans +=1

for i in range(N):
    for j in range(N):
        if pic[i][j] == "R":
            pic[i][j] ="G"


visited = [[False] * N for _ in range(N)]
ans1 = 0
for i in range(N):
    for j in range(N):
        if pic[i][j] == "B" and not visited[i][j]:
            bfs(i,j,"B")
            ans1 +=1
        elif pic[i][j] == "G" and not visited[i][j]:
            bfs(i,j,"G")
            ans1 +=1
print(ans,ans1)

            