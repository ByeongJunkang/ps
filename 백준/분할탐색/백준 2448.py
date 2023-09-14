n = int(input())
tmp_space = [[' '] * 2*n for _ in range(n)]
def fill(x,y,n):
    print(x,y,n)
    if n == 3:
        for j in range(-2,3):
            tmp_space[x+2][y+j] = "*"
        tmp_space[x][y] ="*"
        tmp_space[x+1][y+1] = "*"
        tmp_space[x+1][y-1] = "*"
           
    else:
        newSize = n//2
        fill(x, y, newSize)
        fill(x + newSize, y - newSize, newSize)
        fill(x + newSize, y + newSize, newSize)

        
fill(0,n-1,n)

for star in tmp_space:
    print("".join(star))