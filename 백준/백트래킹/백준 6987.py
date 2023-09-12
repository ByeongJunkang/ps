from itertools import combinations
game = list(combinations(range(6),2))
def dfs(cnt):
    global ans
    if cnt == 15:
        ans = 1
        for sub in res:
            if sub.count(0) != 3:
                ans = 0
                break
        return
    i,j = game[cnt]
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if res[i][x] >0 and res[j][y]>0:
            res[i][x] -=1
            res[j][y] -=1  
            dfs(cnt+1)
            res[i][x] += 1
            res[j][y] += 1   

            
answer = []
for _ in range(4):
    data = list(map(int, input().split()))
    res = [data[i:i + 3] for i in range(0, 16, 3)]
    # print(res)
    ans = 0
    dfs(0)
    answer.append(ans)
print(*answer)