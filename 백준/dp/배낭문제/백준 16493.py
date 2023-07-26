N,M = map(int,input().split())
books = []
for _ in range(M):
    a,b = map(int,input().split())
    books.append([a,b])


dp = [[0] * (N+1) for _ in range(M+1)]

for i in range(1,M+1):
    days = books[i-1][0]
    pages = books[i-1][1]
    for j in range(1,N+1):
        if days > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-days] + pages,dp[i-1][j])


print(dp[M][N])