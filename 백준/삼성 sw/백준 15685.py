n = int(input())
board = [[0] * 101 for _ in range(101)]
coor = set()
tmp = []
for _ in range(n):
    y,x,d,g= map(int,input().split())
    cur = 0
    tmp =[(x,y)]
    tmp_tmp = []
    start_x,start_y= x,y
    while cur < g + 1:
        if cur ==0:
            if d == 0:
                tmp.append((x,y+1))
                start_x,start_y = x,y+1
            elif d == 1:
                tmp.append((x-1,y))
                start_x,start_y = x-1,y
            elif d == 2:
                tmp.append((x,y-1))
                start_x,start_y = x,y-1
            elif d == 3:
                tmp.append((x+1,y))
                start_x,start_y = x+1,y

            cur +=1

        else:
            for idx in tmp:
                idx_x,idx_y = idx[0],idx[1]
                dx,dy = start_x-idx_x,start_y -idx_y
                tmp_tmp.append((start_x - dy,start_y+dx))

            for i in tmp_tmp:
                if i not in tmp:
                    tmp.append(i)
            cur+=1

            start_x,start_y = tmp[-1] 
        print(start_x,start_y)
    print(tmp)
    for i in tmp:
        if i not in coor:
            coor.add(i)
print(coor)