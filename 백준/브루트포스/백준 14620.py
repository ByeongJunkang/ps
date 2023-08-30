from itertools import combinations
N = int(input())
flower = [list(map(int,input().split())) for _ in range(N)]
temp = []
for i in range(1,N-1):
    for j in range(1,N-1):
        temp.append((i,j))
dx = [0,1,0,-1,0]
dy = [0,0,1,0,-1]
temp1 = list(combinations(temp,3))
min_num = 10**10

for num in temp1:
    board = set()
    isTrue = True
    temp_num = 0
    for cor in num:
        cur_x,cur_y = cor[0],cor[1]
        for i in range(5):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i] 
            if (next_x,next_y) not in board:
                board.add((next_x,next_y))
                temp_num += flower[next_x][next_y]
            else:
                break

    if len(board) == 15:
        min_num = min(temp_num,min_num)
            
print(min_num)
