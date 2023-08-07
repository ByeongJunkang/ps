N,M = map(int,input().split())
num_list = sorted(list(map(int,input().split())))
result = []
real_result = []
def dfs(i):

    if len(result) == M:
        real_result.append(result[:])
        return
    
    for num in range(i,N):
        result.append(num_list[num])
        dfs(num)
        result.pop()


dfs(0)
real_result = sorted(list(map(list,set(map(tuple,real_result)))))
for list in real_result:
    print(*list)