import sys
n,k = map(int,input().split())
col = 0
row = n
isTrue = False
while col <= row:
    c_cut = (col + row) //2
    r_cut = n - c_cut
    piece = (c_cut+1) * (r_cut+1)
    if piece == k:
        print("YES")
        isTre = True
        sys.exit()
    else:
        if k > piece:
            col = c_cut + 1
        else:
            row = c_cut - 1



if not isTrue:
    print("NO")