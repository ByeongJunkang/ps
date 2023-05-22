N = int(input())

dp = [0] * (N+1)
dp1 = [0] * (N+1)

for i in range(1,(N+1)):
    dp[i] = int(input())

if(N == 1):
    print(dp[1])
elif(N==2):
    print(dp[2]+dp[1])

else:
   

    dp1[1] = dp[1]
    dp1[2] = dp[1]+dp[2]

    for i in range(3,(N+1)):
        dp1[i] = max(dp1[i-1],dp1[i-2]+dp[i],dp1[i-3]+dp[i-1]+dp[i])

    print(dp1[N-1])