n = int(input())
dp  = [[0] * n for _ in range(n)]
num = []
for _ in range(n):
    a = list(map(int,input().split()))
    num.append(a)
dp[0][0] = num[0][0]
for i in range(1,len(num)):
    for j in range(len(num[i])):
        if j == 0 :
            dp[i][j] = num[i][j] + dp[i-1][j]
        elif j == len(num[i]) - 1:
            dp[i][j] = num[i][j] + dp[i-1][j-1]

        else:
            dp[i][j] = num[i][j] + max(dp[i-1][j-1],dp[i-1][j])

print(max(dp[n-1]))