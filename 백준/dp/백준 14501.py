N = int(input())
work = [list(map(int,input().split())) for _ in range(N)]
dp = [0] * N
def find_max(arr,num):
    max = 0
    for i in range(0,num):
        if arr[i] > max:
            max = arr[i]
    return max
for i in range(N):
    sum = 0
    
    if i + work[i][0] < N:
        max_num = find_max(dp,i)
        dp[i + work[i][0]-1] = max(max_num + work[i][1],dp[i+work[i][0]-1])
    elif i + work[i][0]  == N:
        max_num = find_max(dp,i)
        dp[i + work[i][0]-1] = max(max_num + work[i][1],dp[i+work[i][0]-1])
    
print(max(dp))