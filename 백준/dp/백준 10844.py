# from itertools import permutations
# N = int(input())
# need_list = []
# count = 0
# def permutation():
#     global count
#     if len(need_list) == N:
#         isone = True
#         if need_list[0] != 0:
#             for i in range(N-1):     
#                 if i+1 < N:
#                     left = need_list[i+1]
#                     front = need_list[i]
#                     if front - left == 1 or front - left == -1:
#                         isone = True
#                     else:
#                         isone = False
#                         break
#             if isone == True:
#                 count +=1

#         return
    
#     for i in range(10):
#         need_list.append(i)
#         permutation()
#         need_list.pop()



# permutation()
# print(count)
# list = {}

N = int(input())
dp = [[0]*10 for _ in range(N+1)]
for i in range(1,10):
    dp[1][i] = 1

for i in range(2,N+1):
    for j in range(0,10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % 1000000000)