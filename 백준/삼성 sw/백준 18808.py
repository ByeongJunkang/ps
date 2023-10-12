import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
notebook = [[0] * m for _ in range(n)]

def check(x,y):
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1 and notebook[x+i][y+j] == 1:
                return False
            

    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                notebook[x+i][y+j] = 1
    
    return True


def rotate(sticker):
    n,m = len(sticker),len(sticker[0])
    new_sticker = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            new_sticker[i][j] = sticker[n-1-j][i]

    return new_sticker    



for _ in range(k):
    r,c = map(int,input().split())
    sticker = [list(map(int,input().split())) for _ in range(r)]
    
    for _ in range(4):
        is_paste = False
        r,c = len(sticker),len(sticker[0])
        for i in range(n-r+1):
            if is_paste:
                break
            for j in range(m-c+1):
                if check(i,j):
                    is_paste = True
                    break
        if is_paste:
            break
        sticker = rotate(sticker)

                            
ans = 0
for i in range(n):
    for j in range(m):
        if notebook[i][j] == 1:
            ans +=1
print(ans)
