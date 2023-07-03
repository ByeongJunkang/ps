# from collections import deque
# m,n = map(int,input().split())
# land = [list(map(int,input().split())) for _ in range(n)]


# dx = [0,0,1,-1]
# dy = [-1,1,0,0]
# visited = [[-1] * m for _ in range(n)]
# def bfs(i,j):
#     queue = deque()
#     visited[i][j] = 0
#     queue.append((i,j))
#     while queue:
#         cur_x,cur_y = queue.popleft()
#         for k in range(4):
#             next_x = cur_x + dx[k]
#             next_y = cur_y + dy[k]
#             if next_x >=0 and next_x <n and next_y >=0 and next_y < m and visited[next_x][next_y] == -1:
#                 if land[next_x][next_y] == 0:
#                     visited[next_x][next_y] = 0
#                 elif land[next_x][next_y] == 1:
#                     queue.append((next_x,next_y))
#                     visited[next_x][next_y] = visited[cur_x][cur_y] +1

 


# for i in range(n):
#     for j in range(m):
#         if land[i][j] ==2 and visited[i][j] == -1:
#             bfs(i,j)

# for i in visited:
#     for j in i:
#         print(j, end= ' ')
#     print()



from collections import deque
import sys
input = sys.stdin.readline

d = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(y,x):  
    queue = deque()
    queue.append([y,x])
    visited[y][x] = 0
    while queue:
        r, c =  queue.popleft()
    
        for i in range(4):
            rr = r+d[i][0]
            cc = c+d[i][1]
            
            if (0<=rr<n) and (0<=cc<m) and visited[rr][cc] == -1: 
                if graph[rr][cc] == 0:
                    visited[rr][cc] = 0
                elif graph[rr][cc] == 1: 
                    visited[rr][cc] = visited[r][c] +1
                    queue.append([rr,cc])
n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
for i in range(n):
    for k in range(m):
        if graph[i][k] == 2 and visited[i][k]== -1:
            bfs(i,k)
for i in range(n):
    for k in range(m):
        if graph[i][k] == 0:
            print(0, end= " ")
        else:
            print(visited[i][k], end = " ")
    print()