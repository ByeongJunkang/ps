import math
n, k = map(int,input().split())
coin = [0]
for _ in range(n):
    coin.append(int(input()))

dp = [[math.inf] * (k+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,k+1):
        if coin[i] == j:
            dp[i][j] = 1
            continue
        if coin[i] < j:
            dp[i][j] =  min(dp[i-1][j], dp[i][j-coin[i]]+1)
        else:
            dp[i][j] = dp[i-1][j]
        
if dp[n][k] == math.inf:
    print(-1)
else:
    print(dp[n][k])
