N = int(input())
dp = [1] * 91
dp[2] = 1
for i in range(3,91):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[N])