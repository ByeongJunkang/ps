# N ,M = map(int,input().split())
# need_list = []
# result = []
# def combination(arr,n):
#     result = []
#     if n == 0:
#         return [[]]
    
#     for i in range(len(arr)):
#         elem = arr[i]

#         for rest in combination(arr[i+1:],n-1):
#             result.append([elem]+rest)
    
#     return result

# arr = [list(map(int,input().split())) for _ in range(N)]
# chicken = []
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 2:
#             chicken.append((i,j))

# a = (combination(chicken,M))
# candidate = []
# for i in a:
#     visited = [[9999999] * N for _ in range(N)]
#     for h in i:
#         cur_x = h[0]
#         cur_y = h[1]
#         for j in range(N):
#             for k in range(N):
#                 if arr[j][k] == 1:
#                     visited[j][k] = min(visited[j][k],(abs(cur_x - j)+abs(cur_y-k) ))
#         sum = 0
#         for i in range(N):
#             for j in range(N):
#                 if visited[i][j] != 9999999:
#                     sum += visited[i][j]
#         candidate.append(sum)



# print(min(candidate))
from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chicken = []
houses = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            houses.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

candidate = float('inf')

for selected_chickens in combinations(chicken, M):
    total_distance = 0

    for house_x, house_y in houses:
        distance = float('inf')

        for chicken_x, chicken_y in selected_chickens:
            distance = min(distance, abs(chicken_x - house_x) + abs(chicken_y - house_y))

        total_distance += distance

    candidate = min(candidate, total_distance)

print(candidate)



