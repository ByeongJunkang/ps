# N,M = map(int,input().split())
# trip = [list(map(int,input().split())) for _ in range(N)]

# dp = [[9999999] * M for _ in range(N)]
# dx = [-1,-1,-1]
# dy = [-1,0,1]
# direction = [[-1] * M for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         if i == 0:
#             dp[0][j] = trip[0][j]
#         elif i == 1:
#             if j == 0:
#                 for k in range(3):
#                     if k == 0:
#                         continue
#                     next = trip[i][j] + dp[i+dx[k]][j+dy[k]]
#                     if next < dp[i][j]:
#                         dp[i][j] = next
#                         direction[i][j] = k
#             elif j == M-1:
#                  for k in range(3):
#                     if k == 2:
#                         continue
#                     next = trip[i][j] + dp[i+dx[k]][j+dy[k]]
#                     if next < dp[i][j]:
#                         dp[i][j] = next
#                         direction[i][j] = k
#             else:
#                 for k in range(3):
#                     next = trip[i][j] + dp[i+dx[k]][j+dy[k]]
#                     if next < dp[i][j]:
#                         dp[i][j] = next
#                         direction[i][j] = k 
            

#         else:
#             if j == 0:
#                 temp = 0
#                 for k in range(3):
#                     if k == 0:
#                         continue
                    
#                     next = trip[i][j] + dp[i+dx[k]][j+dy[k]]
#                     if direction[i+dx[k]][j+dy[k]] == k:
#                         continue
#                     if next < dp[i][j]:
#                         dp[i][j] = next
#                         temp = k
#                 direction[i][j] = temp
#             elif j == M-1:
#                 temp = 0
#                 for k in range(3):
#                     if k == 2:
#                         continue
                
#                     next = trip[i][j] + dp[i+dx[k]][j+dy[k]]
#                     if direction[i+dx[k]][j+dy[k]] == k:
#                         continue
#                     if next < dp[i][j]:
#                         dp[i][j] = next
#                         temp = k
#                 direction[i][j] = temp
#             else:
#                 temp =0
#                 for k in range(3):
#                     next = trip[i][j] + dp[i+dx[k]][j+dy[k]]
#                     if direction[i+dx[k]][j+dy[k]] == k:
#                         continue
#                     if next < dp[i][j]:
#                         dp[i][j] = next
#                         temp = k 
#                 direction[i][j] = temp

# print(dp)
# print(min(dp[N-1]))

import sys
input = sys.stdin.readline




N, M = map(int, input().split())
trip = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0,0,0] for _ in range(M)]] + [[[float('inf'),float('inf'),float('inf')] for _ in range(M)] for _ in range(N)]

for i in range(1,N+1):
    for j in range(M):
        if j < M-1:
            dp[i][j][0] = min(dp[i-1][j+1][1],dp[i-1][j+1][2]) + trip[i-1][j]
        if 0 < j:
            dp[i][j][2] = min(dp[i-1][j-1][1],dp[i-1][j-1][0]) + trip[i-1][j]
        dp[i][j][1] = min(dp[i-1][j][0],dp[i-1][j][2]) + trip[i-1][j]




min_value = float('inf')
for row in dp[i]:
    for each in row:
        min_value = min(min_value,each)
print(min_value)

