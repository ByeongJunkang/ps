from itertools import combinations
n = int(input())
pic = [list(input()) for _ in range(5*n)]
tmp = [i for i in range(n)]
result = []
ans = 10**9
for num in sorted(combinations(tmp,2)):
    first = num[0]
    second = num[1]
    tmp = 0
    for i in range(5):
        for j in range(7):
            if pic[5*first+i][j] != pic[5*second+i][j]:
                tmp +=1
    
    if ans > tmp:
        result = [first+1,second+1]
        ans = tmp
    
print(*result)