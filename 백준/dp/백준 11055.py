N = int(input())
num = list(map(int,input().split()))
sum = [0] * N
sum[0] = num[0]
for i in range(1,N):
    max_index = 0
    max_sum = 0
    for j in range(i):
        if num[j] < num[i]:
            max_sum = max(max_sum,sum[j] + num[i])
    if max_sum == 0:
        sum[i] = num[i]
    else:
        sum[i] = max_sum

print(max(sum))
    