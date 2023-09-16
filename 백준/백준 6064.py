t= int(input())

for _ in range(t):
    m,n,x,y = map(int,input().split())
    tmp = set()
    first_x,first_y = 0,0

    cnt = 0
    while True:
        if first_x == x and first_y == y:
            print(cnt)
            break
            
     

        if first_x < m:
            first_x = first_x + 1
        else:
            first_x = 1
        
        if first_y < n:
            first_y = first_y + 1
        else:
            first_y = 1
        cnt +=1
        if (first_x,first_y) in tmp:
            print(-1)
            break
        else:
            tmp.add((first_x,first_y))
        
