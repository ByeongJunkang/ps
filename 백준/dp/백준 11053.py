A = int(input())
num = list(map(int,input().split()))
dp = [0] * (A+1)
dp[0] = 1

for i in range(1,A):
    max_index = True
    max_num = 0
    for j in range(i):
        if num[i] > num[j]:
            if num[j] >= max_num:
                max_num = max(dp[j],max_num)
                max_index = False
    if max_index:
        dp[i] = 1
    else:
        dp[i] = max_num+ 1

print(max(dp))
            