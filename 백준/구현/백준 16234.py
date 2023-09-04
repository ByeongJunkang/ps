from collections import deque
n,l,r = map(int,input().split())
people = [list(map(int,input().split())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def bfs(i,j,visited):
    q = deque()
    q.append((i,j))
    result = []
    result.append((i,j,people[i][j]))
    visited[i][j] = True
    while q:
        cur_x,cur_y = q.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0 <=next_x < n and 0 <= next_y < n:
                if l <= abs(people[cur_x][cur_y] -people[next_x][next_y]) <= r and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    q.append((next_x,next_y))
                    result.append((next_x,next_y,result[-1][2] + people[next_x][next_y]))
    for tmp in result:
        x,y = tmp[0],tmp[1]
        people[x][y] = result[-1][2] // len(result)
    if len(result) == 1:
        return 0
    else:
        return 1
     
day = 0
while True:
    flag = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                flag += bfs(i,j,visited)

    if flag == 0:
        break
    else:
        day +=1
    
print(day)