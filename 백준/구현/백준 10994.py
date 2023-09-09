n = int(input())
tmp_num = (4 * n -3) 
tmp = [[" "] * (tmp_num) for _ in range(tmp_num)]
def dfs(x,y,num):
    value = num * 4 - 3 
    for i in range(value):
        if i ==  0 or i == value-1:
            for j in range(value):
                tmp[x+i][y+j] ="*"
        else:
            tmp[x+i][y] = "*"
            tmp[x+i][y+value-1] = "*"
x,y = 0,0
while n  > 0:
    dfs(x,y,n)
    x+=2
    y+=2
    n -=1

for i in range(len(tmp)):
    for j in range(len(tmp[0])):
        print(tmp[i][j],end="")
    print("")

# print(tmp)