from collections import deque
n, m = map(int,input().split())
paper = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
def bfs(a,b):
    count = 1
    queue = deque()
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    queue.append((a,b))
    visited[a][b] = True
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if (next_x >=0 and next_y >=0 and next_x < n and next_y < m):
                if (paper[next_x][next_y]) == 1 and not visited[next_x][next_y]:
                    count +=1
                    visited[next_x][next_y] = True
                    queue.append((next_x,next_y))

    return count

answer = []
for i in range(n):
    for j in range(m):
        if paper[i][j] ==1 and not visited[i][j]:
            answer.append(bfs(i,j))

if len(answer) == 0:
    print(0)
    print(0)
else:
    print(len(answer))
    print(max(answer))