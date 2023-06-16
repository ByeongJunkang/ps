# N = int(input())
# dp = [1 for _ in range(N)]
# boxes = list(map(int,input().split()))
# def max_list(a,num):
#     max_num = 0
#     index = 0
#     for i in range(a):
#         if boxes[i] >= max_num: 
#             if boxes[i] < num:
#                 max_num = boxes[i]
#                 index = i        
#     return (index,max_num)

# for i in range(1,N):
#     max_index,max_num = max_list(i,boxes[i])
#     if max_num != 0:
#         dp[i] = dp[max_index] + 1

# print(dp)
# print(max(dp))


n = int(input())
box = list(map(int, input().split()))
dp = [1 for _ in range(n)]
for i in range(1,n):
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))