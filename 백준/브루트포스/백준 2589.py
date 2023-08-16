from collections import deque
L,W = map(int,input().split())

treasure_map = [list(input()) for _ in range(L)]
land_list = []
for i in range(L):
    for j in range(W):
        if treasure_map[i][j] == 'L':
            land_list.append([i,j])



max_num = 0
def bfs(i,j) : 
    global max_num
    q= deque()
    q.append((i,j,0))
    visited = [[False] * W for _ in range(L)]
    visited[i][j] = True
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    while q:
        cur_x, cur_y,cur_len = q.popleft()
        for k in range(4):
            next_x = cur_x + dx[k]
            next_y = cur_y + dy[k]
            if next_x >=0 and next_x < L and next_y >=0 and next_y < W:
                if not visited[next_x][next_y] and treasure_map[next_x][next_y] == "L":
                    q.append((next_x,next_y,cur_len+1))
                    max_num = max(max_num,cur_len+1)
                    visited[next_x][next_y] = True

for i in range(L):
    for j in range(W):
        if treasure_map[i][j] == "L":
            bfs(i,j)
print(max_num)