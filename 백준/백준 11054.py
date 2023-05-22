N = int(input())

arr = list(map(int,input().split()))



dp_up = [0] * (N)
dp_down = [0] *(N)

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j] and dp_up[i] < dp_up[j]:
            dp_up[i] = dp_up[j]
    dp_up[i] +=1

for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if arr[i] > arr[j] and dp_down[i] < dp_down[j]:
            dp_down[i] = dp_down[j]
    dp_down[i] +=1



dpmix = [0] * N

for i in range(N):
    dpmix[i] = dp_down[i] + dp_up[i]
  
       


print(max(dpmix)-1)





