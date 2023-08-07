N, M = map(int,input().split())
num_list = sorted(list(map(int,input().split())))
new_list = []
result = []
def dfs(num):
    if len(result)  == M:
        new_list.append(result[:])
        return
    
    for i in range(num,N):
            result.append(num_list[i])
            dfs(i+1)
            result.pop()

dfs(0)
new_list = sorted(list(map(list,set(map(tuple,new_list)))))

for i in new_list:
     print(*i)





# 1,7,9
