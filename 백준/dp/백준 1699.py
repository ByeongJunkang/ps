import math
N = int(input())
dp = [math.inf] * (N+1)

for i in range(1,N+1):
    for j in range(1,int(math.sqrt(i))+1):
        num = j**2
        if i == num:
            dp[i] = 1
            break
        else:
            dp[i] = min(dp[i],dp[i-num] + dp[num])

print(dp[N])

# n = int(input())
# dp = [x for x in range (n+1)]
# for i in range(1,n+1):
#     for j in range(1,i):
#         if j*j > i :
#             break
#         if dp[i] > dp[i-j*j] + 1 :
#             dp[i] = dp[i-j*j] + 1
# print(dp[n])