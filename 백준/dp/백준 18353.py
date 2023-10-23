# n명 병사
# 전투력 높은 병사 앞쪽
# 특정 위치 열외, 병사수 최대

n = int(input())
soldiers = list(map(int,input().split()))
dp = [1] *(n)
ans = 0
for i in range(n):
    for j in range(i):
        if soldiers[i] < soldiers[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))