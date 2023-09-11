from collections import deque
M, N, H = map(int,input().split())

total_height = N * H
box = [list(map(int,input().split())) for _ in range(total_height)]
visited = [[False] * M for _ in range(total_height)]
queue = deque()




shortest_length = 0
cnt1 = 0
dx = [1,0,-1,0,N,-N] 
dy = [0,1,0,-1,0,0]
x = 0
y = 0
result= []
def bfs(x,y):
        while queue:
            print(queue)
            cur_x, cur_y= queue.popleft()
            for i in range(6):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if (next_x >=0 and next_y>=0 and next_x <total_height and next_y < M):
                    if box[next_x][next_y] == 0 and not visited[next_x][next_y]:
                        queue.append((next_x,next_y))
                        visited[next_x][next_y] = True
                        box[next_x][next_y] =  box[x][y] + 1
                     
                


for i in range(total_height):
    for j in range(M):
        if box[i][j] == 1 and not visited[i][j]:
            queue.append((i,j))
            visited[i][j] = True

for i in range(total_height):
     for j in range(M):
        bfs(i,j)
print(queue)
print(box) 

# if cnt != cnt1:
#     print(-1)
# else:
#     num1,num2,num3 = queue.pop()
#     print(num3)
# import sys
# from collections import deque

# m, n, h = map(int, input().split())

# matrix = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
# visited = [[[False]*m for _ in range(n)] for _ in range(h)]

# queue = deque()

# dx = [-1,1,0,0,0,0]
# dy = [0,0,-1,1,0,0]
# dz = [0,0,0,0,-1,1]

# answer = 0
# def bfs():
#     while queue:
#         x,y,z = queue.popleft()

#         for i in range(6):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             nz = z + dz[i]

#             if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
#                 continue

#             if matrix[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
#                 queue.append((nx,ny,nz))
#                 matrix[nx][ny][nz] = matrix[x][y][z] + 1
#                 visited[nx][ny][nz] = True



# for a in range(h):
#     for b in range(n):
#         for c in range(m):
#             if matrix[a][b][c] == 1 and visited[a][b][c] == 0:
#                 queue.append((a,b,c))
#                 visited[a][b][c] = True
                
# bfs()

# print(matrix)
# for a in matrix:
#     print(a)
#     for b in a:
#         print(b)
#         for c in b:
#             print(c)
#             if c == 0:
#                 print(-1)
#                 exit(0)            
#         answer = max(answer, max(b))

# print(answer-1)