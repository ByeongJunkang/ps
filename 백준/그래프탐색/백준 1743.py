import sys
sys.setrecursionlimit(10**5)
N,M,K = map(int,input().split())
food = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
for _ in range(K):
    a,b = map(int,input().split())
    food[a-1][b-1] = 1

dx = [1,0,-1,0]
dy = [0,1,0,-1]
answer = []
size = 1
def dfs(x,y): 
    global size
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if next_x >= 0 and next_y >=0 and next_x <N and next_y <M:
            if food[next_x][next_y]  == 1 and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                size +=1
                dfs(next_x,next_y)
    return size
ans = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j] and food[i][j] == 1:
            size = 1
            visited[i][j] = True
            dfs(i,j)
            print(visited)
            ans = max(size,ans)
print(ans)