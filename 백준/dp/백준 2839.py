N = int(input())
dp = [5001] * (N+5)
dp[3] = 1
dp[5] = 1
for i in range(6,N+1):
    dp[i]= min(dp[i-3],dp[i-5])+1
print(dp[N] if dp[N] < 5001 else -1)

    
