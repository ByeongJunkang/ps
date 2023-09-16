n,m = map(int,input().split())

campus = [list(input()) for _ in range(n)]

from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def bfs(x,y):
    ans = 0
    q = deque()
    q.append((x,y))
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    while q:
        cx,cy = q.popleft()
        if campus[cx][cy] == "P":
            ans +=1
        for i in range(4):
            nx,ny = cx+dx[i],cy+dy[i]
            if 0 <= nx < n and 0<= ny < m:
                if not visited[nx][ny] and campus[nx][ny] != "X":
                    visited[nx][ny] = True
                    q.append((nx,ny))

    return ans
result = 0
for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            result = bfs(i,j)
if result == 0:
    print("TT")
else:
    print(result)