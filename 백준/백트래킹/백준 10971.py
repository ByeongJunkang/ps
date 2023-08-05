import math
N = int(input())

cost = []
visited = [False] * N
for _ in range(N):
    cost.append(list(map(int,input().split())))
    
result = math.inf
temp = []

def dfs(start,now,num):
    global temp
    global result
    if num == N:
        if cost[now][start]:
            result = min(result,sum(temp) +cost[now][start])
            return

    for i in range(N):
        if not visited[i] and cost[now][i] != 0:
            visited[i] = True
            temp.append(cost[now][i])     
            dfs(start,i,num+1)
            visited[i] = False
            temp.pop()
            

            

for i in range(N):
    visited[i] = True
    dfs(i,i,1)
    visited[i] = False
print(result)


# import math
# N = int(input())

# cost = []
# visited = [False] * N
# for _ in range(N):
#     cost.append(list(map(int,input().split())))
    
# result = math.inf
# temp = 0
# def dfs(start,now,value,num):
#     global result
#     if num == N:
#         if cost[now][start]:
#             value += cost[now][start]   
#             result = min(value,result)

#         return

#     for i in range(N):
#         if not visited[i] and cost[now][i] != 0:
#             visited[i] = True
#             dfs(start,i,value+ cost[now][i],num+1)
#             visited[i] = False
           
    
            

# for i in range(N):
#     visited[i] = True
#     dfs(i,i,0,1)
#     visited[i] = False
# print(result)