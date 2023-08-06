N,M = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()
result = []
def dfs(i):
    if len(result) == M:
        print(*result)
        return
    for i in range(i,N):
        result.append(num_list[i])
        dfs(i)
        result.pop()
dfs(0)