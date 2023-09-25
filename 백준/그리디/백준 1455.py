n,m = map(int,input().split())

coin = []
for _ in range(n):
    coin.append(list(map(int,input())))

def reverse(x,y):
    for i in range(n):
        for j in range(m):
            if 0 <= i <= x and 0 <= j <= y:
                if coin[i][j] == 1:
                    coin[i][j] = 0
                else:
                    coin[i][j] = 1
cnt = 0 
for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        if coin[i][j] == 1:
            cnt +=1
            reverse(i,j)
print(cnt)
   