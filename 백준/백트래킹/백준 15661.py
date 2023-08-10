import math
N = int(input())
ability = [list(map(int,input().split())) for _ in range(N)]
visited = [False] * N
min_num = math.inf

def cal_team(lst):
    sum_team = 0
    for _i in range(len(lst)):
        for _j in range(len(lst)):
            if _i != _j:
                i, j = lst[_i], lst[_j]
                sum_team += ability[i][j]
    return sum_team


def dfs(num,target,count):
    global min_num 
    if target == count:
        start, link = [], []
        for i in range(N):
            if visited[i] == True:
                start.append(i)
            else:
                link.append(i)
        if len(start) * len(link) == 0:
            return
        temp1 = cal_team(start)
        temp2 = cal_team(link)
        min_num = min(min_num,abs(temp1-temp2))    
        return
    for i in range(num,N):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1,target,count+1)
            visited[i] = False

for i in range(1,N//2+1):
    dfs(0,i,0)

print(min_num)

