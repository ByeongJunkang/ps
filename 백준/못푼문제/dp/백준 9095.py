T = int(input())

dp = [1] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(3,12):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for _ in range(T):
    a = int(input())
    print(dp[a])