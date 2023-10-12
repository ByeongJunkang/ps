# import copy
# from collections import deque
# n,m = map(int,input().split())
# board = []
# for _ in range(n):
#     board.append(list((input())))
# print(board)

# dx = [0,1,0,-1]
# dy = [1,0,-1,0]


# red_loc, blue_loc, output = 0,0,0

# for i in range(n):
#     for j in range(m):
#         if board[i][j] == "R":
#             red_loc = (i,j)
#         elif board[i][j] == "B":
#             blue_loc = (i,j)
        
#         elif board[i][j] == "O":
#             output = (i,j)


# q= deque()
# q.append((red_loc[0],red_loc[1],0,-1))
# visited = [[False]* m for _ in range(n)]
# visited1 = [[False]*m for _ in range(n)]
# ans = 101

# def fill(x,y,dir,rx,ry):

#     while True:
#         if x == rx and y == ry:
#             break
#         if 0 > nx or nx>=n or ny < 0 or ny >=m:
#             break
#         if not visited1[nx][ny] and board[nx][ny] != '#':
#             visited1[nx][ny] = True

# while q:
#     print(q)
#     cnt,rx,ry,bx,by = q.popleft()
    
#     for i in range(4):
#         r_nx ,r_ny = rx + dx[i], ry+ dy[i]
#         b_nx,b_ny =  bx + dx[i], by+ dy[i]
#         while
#         if 0 <= nx < n and 0 <= ny < m:
#             if not visited[nx][ny] and board[nx][ny] != "#" and board[nx][ny] !="B":
#                 if dir == i:
#                     q.append((nx,ny,change,i))
#                     visited[nx][ny] = True
#                 else:
#                     q.append((nx,ny,change+1,i))
#                     visited[nx][ny] = True
# print(visited)  
# if ans == 101:
#     print(-1)
# else:    
#     print(ans)         
                    





        
    