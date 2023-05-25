# N, M = map(int,input().split())

# arr = [list(map(int,input().split())) for _ in range(N)]

# visited = [[999999] * N for _ in range(N)]
# print(arr)
# chick = []
# city = []

# def dfs(i,j):
#     if arr[i][j] == 1:
#         init_i = i
#         init_j = j
#         for i in range(N):
#             for j in range(N):
#                 if arr[i][j] == 2:
#                     chick.append([i,j])
#                     cost = abs(init_i-i)+abs(init_j-j)
#                     visited[init_i][init_j] = min(visited[init_i][init_j],cost)


# for i in range(N):
#     for j in range(N):
#         dfs(i,j)

# print(visited)
        

            
