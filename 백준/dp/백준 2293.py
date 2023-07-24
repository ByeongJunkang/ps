n,k = map(int,input().split())
moneys = []
dp = [0] * 10001
dp[0] = 1
for _ in range(n):
    a = int(input())
    moneys.append(a)
    

for i in range(n):
    for j in range(moneys[i],k+1):
        dp[j] += dp[j-moneys[i]]


print(dp[k])