# 종수 할아버지는 약 반알 먹음
# 약이 N개
# 첫째 날 약 하나 꺼내 반 쪼개서 먹고 다른 조각은 병에 넣음
# 다음 날 반 조각 or 한 조각
# 한 조각 -> W 반 조각 -> H


dp = [[0] * 31 for _ in range(31)]

for i in range(1,31):
    dp[0][i] = 1
for i in range(1,31):
    for j in range(i,31):
        dp[i][j] += dp[i-1][j] + dp[i][j-1]

while True:
    n = int(input())
    if n ==0:
        break
    print(dp[n][n])

# arr = [[0] * 31 for _ in range(31)]
# for i in range(1, 31):
#     arr[0][i] = 1
# for i in range(1, 31):
#     for j in range(i, 31):
#         arr[i][j] += arr[i-1][j] + arr[i][j-1]
# while True:
#     N = int(input())
#     if N == 0:
#         break
#     print(arr[N][N])