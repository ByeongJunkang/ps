import sys
N = int(input())
energy = [(0,0)]

for _ in range(N-1):
    a,b = map(int,input().split())
    energy.append((a,b))

k = int(input())
if N == 1:
    print(0)
    sys.exit()

if N == 2:
    print(energy[1][0])
    sys.exit()
dp =[0] * (N+1)
dp[2] = energy[1][0]
dp[3] = min(energy[1][0] + energy[2][0], energy[1][1])
for i in range(4,N+1):
    dp[i] = min(dp[i-2] + energy[i-2][1],dp[i-1] +energy[i-1][0])


min_num = 10**9
idx = 0
for i in range(1,N-2):
    tmp_dp = dp[:]
    tmp = dp[i+3] - dp[i]
    if tmp > k:
        tmp_dp[i+3] = tmp_dp[i] + k
        for i in range(i+4,N+1):
            tmp_dp[i] = min(tmp_dp[i],tmp_dp[i-1] + energy[i-1][0], tmp_dp[i-2] +energy[i-2][1])

        if min_num > tmp_dp[-1]:
            min_num = tmp_dp[-1]
    

if min_num == 10**9:
    print(dp[-1])
else:
    print(min_num)

