from collections import deque
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
result = [[0] * N for _ in range(N)]

def bfs(i,j):
    visited = [False] * N
    q= deque()
    for x in range(N):
        if board[i][x] == 1 and not visited[x]:
            q.append(x)
            visited[x] =  True
    
    while q:
        cur_x = q.popleft()
        if cur_x==j:
            result[i][j] = 1
            break
        for x in range(N):
            if board[cur_x][x] ==1 and not visited[x]:
                q.append(x)
                visited[x] = True


for i in range(N):
    for j in range(N):
        bfs(i,j)

for i in result:
    print(*i)
