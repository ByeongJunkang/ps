n = int(input())
List = list(map(int,input().split()))

dp = [0] * n
dp [0] = List[0]
for i in range(1,n):
    dp[i] = max(List[i],dp[i-1]+List[i])

print(max(dp))