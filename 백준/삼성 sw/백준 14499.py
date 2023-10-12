n,m,x,y,k = map(int,input().split())
board = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    board.append(tmp)
dir = list(map(int,input().split()))
dice = [[0]* 3 for _ in range(4)]

def roll_dice(dice,dir):
    new_dice = [[0] * 3 for _ in range(4)]
    if dir == 1:
        #ok
        new_dice[0][1] = dice[0][1]
        #ok
        new_dice[1][1] = dice[1][0]
        #ok
        new_dice[2][1] = dice[2][1]
        #ok
        new_dice[3][1] = dice[1][2]
        #ok
        new_dice[1][0] = dice[3][1]
        #ok
        new_dice[1][2] = dice[1][1]

    elif dir ==2:
        # ok
        new_dice[0][1] = dice[0][1]
        #ok
        new_dice[1][1] = dice[1][2]
        #ok
        new_dice[2][1] = dice[2][1]
        #ok
        new_dice[3][1] = dice[1][0]
        #ok
        new_dice[1][0] = dice[1][1]
        #ok
        new_dice[1][2] = dice[3][1]
    
    elif dir == 4:
        #ok
        new_dice[0][1] = dice[3][1]
        #ok
        new_dice[1][1] = dice[0][1]
        #ok
        new_dice[2][1] = dice[1][1]
        #ok
        new_dice[3][1] = dice[2][1]
        #ok
        new_dice[1][0] = dice[1][0]
        #ok
        new_dice[1][2] = dice[1][2]
    
    elif dir == 3:
        new_dice[0][1] = dice[1][1]
        new_dice[1][1] = dice[2][1]
        new_dice[2][1] = dice[3][1]
        new_dice[3][1] = dice[0][1]
        new_dice[1][0] = dice[1][0]
        new_dice[1][2] = dice[1][2]
    
    return new_dice


cx,cy = x,y
for i in dir:
    flag = False
    if i == 1:
        if 0 <=cx < n and 0 <= cy+1 < m:
            dice = roll_dice(dice,i)
            flag = True
            cy = cy +1    
    elif i == 2:
        if 0 <=cx < n and 0 <= cy -1 < m:
            dice = roll_dice(dice,i)
            flag = True
            cy = cy - 1
    elif i == 4:
        if 0 <=cx + 1 < n and 0 <= cy < m:
            dice = roll_dice(dice,i)
            cx = cx + 1
            flag = True
    elif i == 3:
        if 0 <=cx - 1< n and 0 <= cy < m:
            dice = roll_dice(dice,i)
            cx = cx - 1
            flag = True

    
    if flag:
        if board[cx][cy] == 0:
            board[cx][cy] = dice[3][1]
        else:
            dice[3][1] = board[cx][cy]
            board[cx][cy] = 0
        print(dice[1][1])

