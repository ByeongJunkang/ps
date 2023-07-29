N = int(input())
pattern =[['*'] * (N) for _ in range(N)]
def erase(x,y,N):
    
    if N < 3:
        return
    
    for i in range(x+N//3,x+N//3*2):
        for j in range(y+N//3,y+N//3*2):
            pattern[i][j] = ''

    for i in range(3):
        for j in range(3):
            erase(x+N//3*i,y+N//3*j,N//3)

erase(0,0,N)
for i in pattern:
    for j in i:
        if j == '*':
            print(j,end='')
        else:
            print(' ', end='')
    print()
