import sys
input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))

answer = 0
dp = [[-1] * m for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
visited = [[False] * m for _ in range(n)]
def dfs(x,y):
    if x == n-1 and y == m-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    ans = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[x][y] > graph[nx][ny]:
            ans += dfs(nx,ny)

    dp[x][y] = ans
    return dp[x][y]  

print(dfs(0,0))
