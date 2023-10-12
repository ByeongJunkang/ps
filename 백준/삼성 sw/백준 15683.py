# from itertools import product
# import copy
# n ,m = map(int,input().split())
# place = [list(map(int,input().split())) for _ in range(n)]


# cctv = []
# for i in range(n):
#     for j in range(m):
#         if place[i][j] != 0 and place[i][j] != 6:
#             cctv.append((place[i][j],(i,j)))
# tmp_result = list(product([0,1,2,3],repeat=len(cctv)))
# answer = 65
# for tmp_dir in tmp_result:
#     land = copy.deepcopy(place)

#     for dir in range(len(tmp_dir)):
#         direction = tmp_dir[dir]
#         if cctv[dir][0] == 1:
#             cur_x,cur_y = cctv[dir][1]
#             while 0<=cur_x < n and 0<=cur_y <m:
#                 if land[cur_x][cur_y] == 6:
#                     break
#                 if land[cur_x][cur_y] == 0:
#                     land[cur_x][cur_y] = '#'
#                 cur_x += first[direction][0]
#                 cur_y += first[direction][1]
#         elif cctv[dir][0] == 2:
#             cur_x,cur_y = cctv[dir][1]
#             next_x1,next_y1 = cur_x,cur_y
#             next_x2,next_y2 = cur_x,cur_y
#             while 0<=next_x1 < n and 0<=next_y1 <m:
#                 if land[next_x1][next_y1] == 6:
#                     break
#                 if land[next_x1][next_y1] == 0:
#                     land[next_x1][next_y1] = '#'
#                 next_x1 += second[direction][0][0]
#                 next_y1 += second[direction][0][1]
#             while 0<=next_x2 < n and 0<=next_y2 <m:
#                 if land[next_x2][next_y2] == 6:
#                     break
#                 if land[next_x2][next_y2] == 0:
#                     land[next_x2][next_y2] = '#'
#                 next_x2 += second[direction][1][0]
#                 next_y2 += second[direction][1][1]


#         elif cctv[dir][0] == 3:
#             cur_x,cur_y = cctv[dir][1]
#             next_x1,next_y1 = cur_x,cur_y
#             next_x2,next_y2 = cur_x,cur_y
#             while 0<=next_x1 < n and 0<=next_y1 <m:
#                 if land[next_x1][next_y1] == 6:
#                     break
#                 if land[next_x1][next_y1] == 0:
#                     land[next_x1][next_y1] = '#'
#                 next_x1 += third[direction][0][0]
#                 next_y1 += third[direction][0][1]
#             while 0<=next_x2 < n and 0<=next_y2 <m:
#                 if land[next_x2][next_y2] == 6:
#                     break
#                 if land[next_x2][next_y2] == 0:
#                     land[next_x2][next_y2] = '#'
#                 next_x2 += third[direction][1][0]
#                 next_y2 += third[direction][1][1]


#         elif cctv[dir][0] == 4:
#             cur_x,cur_y = cctv[dir][1]
#             cur_x,cur_y = cctv[dir][1]
#             nx1,ny1 = cur_x,cur_y
#             nx2,ny2 = cur_x,cur_y
#             nx3,ny3 = cur_x,cur_y
#             if direction == 0:
#                 while 0<=nx1 < n and 0<=ny1 <m:
#                     if land[nx1][ny1] == 6:
#                         break
#                     if land[nx1][ny1] == 0:
#                         land[nx1][ny1] = '#'
#                     nx1 += first[0][0]
#                     ny1 += first[0][1]
#                 while 0<=nx2 < n and 0<=ny2 <m:
#                     if land[nx2][ny2] == 6:
#                         break
#                     if land[nx2][ny2] == 0:
#                         land[nx2][ny2] = '#'
#                     nx2 += first[3][0]
#                     ny2 += first[3][1]
#                 while 0<=nx3 < n and 0<=ny3 <m:
#                     if land[nx3][ny3] == 6:
#                         break
#                     if land[nx3][ny3] == 0:
#                         land[nx3][ny3] = '#'
#                     nx3 += first[2][0]
#                     ny3 += first[2][1]
            
#             elif direction == 1:
#                 while 0<=nx1 < n and 0<=ny1 <m:
#                     if land[nx1][ny1] == 6:
#                         break
#                     if land[nx1][ny1] == 0:
#                         land[nx1][ny1] = '#'
#                     nx1 += first[3][0]
#                     ny1 += first[3][1]
#                 while 0<=nx2 < n and 0<=ny2 <m:
#                     if land[nx2][ny2] == 6:
#                         break
#                     if land[nx2][ny2] == 0:
#                         land[nx2][ny2] = '#'
#                     nx2 += first[1][0]
#                     ny2 += first[1][1]
#                 while 0<=nx3 < n and 0<=ny3 <m:
#                     if land[nx3][ny3] == 6:
#                         break
#                     if land[nx3][ny3] == 0:
#                         land[nx3][ny3] = '#'
#                     nx3 += first[0][0]
#                     ny3 += first[0][1]

#             elif direction == 2:
#                 while 0<=nx1 < n and 0<=ny1 <m:
#                     if land[nx1][ny1] == 6:
#                         break
#                     if land[nx1][ny1] == 0:
#                         land[nx1][ny1] = '#'
#                     nx1 += first[3][0]
#                     ny1 += first[3][1]
#                 while 0<=nx2 < n and 0<=ny2 <m:
#                     if land[nx2][ny2] == 6:
#                         break
#                     if land[nx2][ny2] == 0:
#                         land[nx2][ny2] = '#'
#                     nx2 += first[2][0]
#                     ny2 += first[2][1]
#                 while 0<=nx3 < n and 0<=ny3 <m:
#                     if land[nx3][ny3] == 6:
#                         break
#                     if land[nx3][ny3] == 0:
#                         land[nx3][ny3] = '#'
#                     nx3 += first[1][0]
#                     ny3 += first[1][1]
#             elif direction == 3:
#                 while 0<=nx1 < n and 0<=ny1 <m:
#                     if land[nx1][ny1] == 6:
#                         break
#                     if land[nx1][ny1] == 0:
#                         land[nx1][ny1] = '#'
#                     nx1 += first[2][0]
#                     ny1 += first[2][1]
#                 while 0<=nx2 < n and 0<=ny2 <m:
#                     if land[nx2][ny2] == 6:
#                         break
#                     if land[nx2][ny2] == 0:
#                         land[nx2][ny2] = '#'
#                     nx2 += first[1][0]
#                     ny2 += first[1][1]
#                 while 0<=nx3 < n and 0<=ny3 <m:
#                     if land[nx3][ny3] == 6:
#                         break
#                     if land[nx3][ny3] == 0:
#                         land[nx3][ny3] = '#'
#                     nx3 += first[0][0]
#                     ny3 += first[0][1]        


#         elif cctv[dir][0] == 5:
#             cur_x,cur_y = cctv[dir][1]
#             nx1,ny1 = cur_x,cur_y
#             nx2,ny2 = cur_x,cur_y
#             nx3,ny3 = cur_x,cur_y
#             nx4,ny4 = cur_x,cur_y
#             while 0<=nx1 < n and 0<=ny1 <m:
#                 if land[nx1][ny1] == 6:
#                     break
#                 if land[nx1][ny1] == 0:
#                     land[nx1][ny1] = '#'
#                 nx1 += first[0][0]
#                 ny1 += first[0][1]
#             while 0<=nx2 < n and 0<=ny2 <m:
#                 if land[nx2][ny2] == 6:
#                     break
#                 if land[nx2][ny2] == 0:
#                     land[nx2][ny2] = '#'
#                 nx2 += first[1][0]
#                 ny2 += first[1][1]
#             while 0<=nx3 < n and 0<=ny3 <m:
#                 if land[nx3][ny3] == 6:
#                     break
#                 if land[nx3][ny3] == 0:
#                     land[nx3][ny3] = '#'
#                 nx3 += first[2][0]
#                 ny3 += first[2][1]
#             while 0<=nx4 < n and 0<=ny4 <m:
#                 if land[nx4][ny4] == 6:
#                     break
#                 if land[nx4][ny4] == 0:
#                     land[nx4][ny4] = '#'
#                 nx4 += first[3][0]
#                 ny4 += first[3][1]
#     tmp_answer = 0
#     for i in range(n):
#         for j in range(m):
#             if land[i][j] == 0:
#                 tmp_answer +=1
#     answer = min(answer,tmp_answer)
      
# print(answer)
        

from itertools import product
import copy

first = [(0,1),(1,0),(0,-1),(-1,0)]
second = [[(0,1),(0,-1)],[(-1,0),(1,0)],[(0,1),(0,-1)],[(-1,0),(1,0)]]
third = [[(-1,0),(0,1)],[(0,1),(1,0)],[(1,0),(0,-1)],[(0,-1),(-1,0)]]
def mark_blocked_cells(land, x, y, dx, dy):
    nx, ny = x + dx, y + dy
    while 0 <= nx < n and 0 <= ny < m and land[nx][ny] != 6:
        if land[nx][ny] == 0:
            land[nx][ny] = '#'
        nx += dx
        ny += dy

n, m = map(int, input().split())
place = [list(map(int, input().split())) for _ in range(n)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

cctv = []
for i in range(n):
    for j in range(m):
        if place[i][j] != 0 and place[i][j] != 6:
            cctv.append((place[i][j], i, j))

tmp_result = product([0, 1, 2, 3], repeat=len(cctv))
answer = float('inf')

for tmp_dir in tmp_result:
    land = copy.deepcopy(place)

    for dir_idx, direction in enumerate(tmp_dir):
        cctv_type, x, y = cctv[dir_idx]
        if cctv_type == 1:
            mark_blocked_cells(land, x, y, *directions[direction])
        elif cctv_type == 2:
            for dx, dy in second[direction]:
                mark_blocked_cells(land, x, y, dx, dy)
        elif cctv_type == 3:
            for dx, dy in third[direction]:
                mark_blocked_cells(land, x, y, dx, dy)
        elif cctv_type == 4:
            for i in range(4):
                if i == direction:
                    continue
                dx, dy = directions[i]
                mark_blocked_cells(land, x, y, dx, dy)
        elif cctv_type == 5:
            for dx, dy in directions:
                mark_blocked_cells(land, x, y, dx, dy)

    tmp_answer = sum(row.count(0) for row in land)
    answer = min(answer, tmp_answer)

print(answer)
