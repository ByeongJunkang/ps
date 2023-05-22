# from collections import deque

# grid = [["1","1","0","1","1"],
#         ["1","1","0","0","0"],
#         ["0","0","1","0","0"],
#         ["1","0","1","1","1"],
#         ["1","0","0","1","0"],
#         ["1","0","0","1","1"],
#          ["1","0","0","0","1"],
#          ["1","0","0","0","1"],
#          ["1","0","0","0","0 "]]

# shortest_len = 0
# def shortest_path(grid):
#     column = len(grid)
#     row = len(grid[0])
#     visited = [[False]*row for _ in range(column)]
#     global shortest_len
#     def bfs(x,y):
#         global count
#         queue = deque()
#         queue.append((x,y,1))
#         global shortest_len
#         while queue:
#             cur_x, cur_y,cur_len = queue.popleft()
#             if(cur_x == column-1 and cur_y == row -1):
#                 shortest_len = cur_len
#                 break
                
#             visited[cur_x][cur_y] = True
#             dx = [1, 0,-1,0,-1,-1, 1, 1]
#             dy = [0,-1, 0,1, 1,-1,-1, 1]
#             for i in range(8):
#                 next_x = cur_x + dx[i]
#                 next_y = cur_y + dy[i]
#                 if(next_x >= 0 and next_x< column and next_y >=0 and next_y <row):
#                     if(grid[next_x][next_y]== "1" and not visited[next_x][next_y]):
#                         queue.append((next_x,next_y,cur_len+1))
#                         visited[next_x][next_y] = True

    

#     for i in range(column):
#         for j in range(row):
#             if(grid[i][j] == "1" and not visited[i][j]):
#                 bfs(i,j)

#     return shortest_len
    

# print(shortest_path(grid))