import math
N = int(input())
ability = [list(map(int,input().split())) for _ in range(N)]
arr = [i for i in range(N)]
from itertools import combinations

a = list(combinations(arr,N//2))
result = [k for k in range(N)]
soccer = math.inf
for start_mem in a:

    link_mem = list(set(result)-set(start_mem))
    combi1 = list(combinations(result,2))
    sum = 0
    sum1 = 0
    for i,j in list(combinations(start_mem,2)):
        sum+= ability[i][j]
        sum+= ability[j][i]
    for i, j in list(combinations(link_mem,2)):
        sum1+=ability[i][j]
        sum1+=ability[j][i]
    
    soccer = min(soccer,abs(sum-sum1))

print(soccer)

# visited = [False  for _ in range(N)]
# def dfs(a,idx):
#     if a == N//2:
#         return
    
#     for i in range(idx,N):
#         if not visited[i]:
#             visited[i]= True
#             dfs(a+1,i+1)
#             visited[i] = False