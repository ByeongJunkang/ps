N = int(input())
cards = [0] + list(map(int,input().split()))
dp = [0] * (N+1)
dp[0] = cards[0]
for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i-j] + cards[j],dp[i] )

print(max(dp))