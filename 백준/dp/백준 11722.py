N = int(input())
num = list(map(int,input().split()))
dp = [0] * N
dp[0] = 1
for i in range(1,N):
    for j in range(i):
        if num[i] < num[j]:
            dp[i] = max(dp[j]+1,dp[i])
        else:
            dp[i] = max(dp[i],1)

print(max(dp))