T = int(input())

dp0 = [0] * 41
dp1 = [0] * 41
dp0[0] = 1
dp0[1] = 0
dp1[1] = 1
dp0[2] = 1
dp1[2] = 1
dp0[3] = 1
dp1[3] = 2

for i in range(4,41):
    dp1[i] = dp1[i-1] + dp1[i-2]
    dp0[i] = dp0[i-1] + dp0[i-2]

for _ in range(T):
    a = int(input())
    print(dp0[a],end=" ")
    print(dp1[a])