N = int(input())
a = sorted([list(map(int, input().split())) for _ in range(N)])

dp_up= [0] * N


for i in range(N):
    for j in range(i):
        if a[i][1] > a[j][1] and dp_up[i] < dp_up[j]:
            dp_up[i] = dp_up[j]
    dp_up[i] +=1


print(dp_up)
print(N-max(dp_up))

# n = int(input())
# a = sorted([list(map(int, input().split())) for _ in range(n)])
# print(a)
# dp = [1] * n
# for i in range(n):
#     for j in range(i):
#         if a[i][1] > a[j][1]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(dp)
# print(n - max(dp))