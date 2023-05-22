n = int(input())
List = [0] * 301
for i in range(n):
    List[i] = int(input())

dp = [0] * 301

dp[0] = List[0]
dp[1] = List[1] + List[0]
dp[2] = max(List[1]+ List[2], List[0] + List[2])
for i in range(3,n):
    dp[i] = max(dp[i-2]+List[i], dp[i-3]+List[i-1]+List[i])


print(dp[n-1])


