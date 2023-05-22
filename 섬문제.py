from collections import deque

grid = [["1","1","0","0","0"],
         ["1","1","0","0","0"],
        ["0","0","1","0","0"],
         ["0","0","0","1","1"]]

def num_of_islands(grid):
    column = len(grid)
    count = 0
    row = len(grid[0])
    print(column)
    print(row)

    visited = [[False]* row  for _ in range(column)]
    print(visited)
    

    def bfs(x,y):
        dx = [ 1, 0 , -1 ,0]
        dy = [ 0, -1 ,0, 1]
        queue = deque()
        queue.append((x,y))
        print(queue)
        while queue:
            cur_x, cur_y = queue.popleft()
            visited[cur_x][cur_y]= True
            print(cur_x,cur_y)
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if(next_x >=0 and next_x < column and next_y >=0 and next_y < row):
                    if(grid[next_x][next_y] == "1" and not visited[next_x][next_y]):
                        queue.append((next_x,next_y))
                        



    for i in range(column):
        for j in range (row):
            if(grid[i][j] == "1" and not visited[i][j]):
                bfs(i,j)
                count += 1

    print("count")
    print(count)









print(num_of_islands(grid))































# def numIsIsland(grid):
#     num_of_island = 0
#     m = len(grid)
#     n = len(grid[0])

#     visited = [[False]*n for _ in range (m)]
    
  
#     def bfs(x,y):
#         dx = [1,0,-1,0]
#         dy = [0,-1,0,1]
    
#         visited[x][y] = True

#         queue = deque()
#         queue.append((x, y))
#         while queue:
#             cur_x, cur_y = queue.popleft()
#             print(cur_x,cur_y)
#             for i in range(4):
#                 next_x = cur_x + dx[i]
#                 next_y = cur_y + dy[i]
#                 if(next_x >= 0 and next_x < m and next_y>=0 and next_y< n):
#                     if(grid[next_x][next_y]!="0" and not visited[next_x][next_y]):
#                         visited[next_x][next_y]=True
#                         print(visited)
#                         queue.append((next_x,next_y))

            

#     for i in range(m):
#         for j in range (n):
        
         
#             if(grid[i][j] == "1" and not visited[i][j]):
#                 num_of_island += 1
#                 bfs(i,j)

#     return num_of_island



# grid = [["1","1","0","0","0"],
#         ["1","1","0","0","0"],
#         ["0","0","1","0","0"],
#         ["0","0","0","1","1"]]


# print(numIsIsland(grid))