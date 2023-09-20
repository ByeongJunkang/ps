n,m = map(int,input().split())
num = [list(map(int,input().split())) for _ in range(n)]
ans = 0
dx = [0,1,-1,0]
dy = [1,0,0,-1]
def dfs(i,j,cur_sum,cur_cnt,visited):
    global ans
    visited.add((i,j))
    if cur_cnt == 4:
        ans = max(ans,cur_sum)
        return
    if cur_cnt == 3:
        cross =[(0,1),(0,-1)]
        cross1 = [(1,0),(-1,0)]
        tmp = sorted(list(visited))
        if tmp[0][1] == tmp[1][1] == tmp[2][1]:
            cx,cy =tmp[1][0],tmp[1][1]
            for next in range(2):
                next_x = cx + cross[next][0]
                next_y = cy + cross[next][1]
                if 0 <= next_x < n and 0 <= next_y <m:
                    ans = max(ans,cur_sum + num[next_x][next_y])
                
        elif tmp[0][0] == tmp[1][0] == tmp[2][0]:
            cx ,cy= tmp[1][0],tmp[1][1]
            for next in range(2):
                next_x = cx + cross1[next][0]
                next_y = cy + cross1[next][1]
                if 0 <= next_x < n and 0 <= next_y <m:
                    ans = max(ans,cur_sum + num[next_x][next_y])
    
    for idx in range(4):
        nx = i + dx[idx]
        ny = j + dy[idx]
        if 0 <= nx < n and 0 <= ny < m:
            if (nx,ny) not in visited:
                visited.add((nx,ny))
                dfs(nx,ny,cur_sum+num[nx][ny],cur_cnt+1,visited)
                visited.remove((nx,ny))

for i in range(n):
    for j in range(m):
        dfs(i,j,num[i][j],1,set())

print(ans)
            