dp = [1] * 1001
n = int(input())
for i in range(2,1001):
    dp[i] = dp[i-1] + 2 * dp[i-2]

print(dp[n] % 10007)