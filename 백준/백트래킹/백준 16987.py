n = int(input())
eggs = [list(map(int,input().split())) for _ in range(n)]
ans = 0
def dfs(cur,eggs):
    global ans
    if cur == n:
        cnt = 0
        for egg in eggs:
            if egg[0] <=0 :
                cnt +=1
        ans = max(ans,cnt)
        return
    
    if eggs[cur][0] <= 0:
        dfs(cur+1,eggs)  
    else:
        flag = True
        for i in range(n):
            if cur != i and eggs[i][0] > 0:
                flag = False
                eggs[i][0] -= eggs[cur][1]
                eggs[cur][0] -= eggs[i][1]
                dfs(cur+1,eggs)
                eggs[i][0] += eggs[cur][1]
                eggs[cur][0] += eggs[i][1]
        if flag:
            dfs(n,eggs)
dfs(0,eggs)
print(ans)