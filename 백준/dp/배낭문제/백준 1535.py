# N명 생각해줌 (1 ~ 20)
# i번째 사람에게 인사 -> + L[i] 체력, - J[i] 기쁨
# 각각 사람에게 최대 1번 말할 수 있음
# Max 기쁨, 체력 = 100, 기쁨 = 0

N = int(input())

agility = list(map(int,input().split()))
happiness = list(map(int,input().split()))

dp = [[0] * (101) for _ in range(N+1)]

for i in range(1,N+1):
    a,b = agility[i-1],happiness[i-1]
    for j in range(1,101):
        if j <= a:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-a] + b, dp[i-1][j])

print(dp[N][100])
