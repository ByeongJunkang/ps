puzzle = [list(map(int,input().split())) for _ in range(9)]

def check(x,y):
    visited = [i for i in range(1,10)]
    first_check = True
    for i in range(9):
        if visited[i] ==1:
            first_check = False
            break
        visited[x][i] = 1
    second_check = True
    visited = [i for i in range(1,10)]

    for i in range(9):
        if visited[i] ==1:
            second_check = False
        visited[i][y] = 1
    third_check = True
    next_x = x//3
    next_y = y//3
    for i in range(3):
        for j in range(3):
            puzzle