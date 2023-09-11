from collections import deque
N = int(input())
map =[list(map(int,input().split())) for _ in range(N)]
def bfs(x,y,rain):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if next_x >=0 and next_y>=0 and next_x < N and next_y < N:
                if map[next_x][next_y] > rain and not visited[next_x][next_y]:
                    queue.append((next_x,next_y))
                    visited[next_x][next_y] = True

max_num = 0                   
for a in map:
  for b in a:
    if max_num < b:
      max_num = b
    
      
result1 = []
for k in range(max_num+1):
    result = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if map[i][j] > k and not visited[i][j]:
                bfs(i,j,k)
                result +=1
    result1.append(result)
    
print(max(result1))