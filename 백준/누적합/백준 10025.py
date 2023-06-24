# from collections import defaultdict
# import math
# N, K = map(int,input().split())
# ice = defaultdict(int)
# max_num = 0
# min_num = math.inf

# for _ in range(N):
#     a,b = map(int,input().split())
#     ice[b] = a
#     max_num = max(b,max_num)
#     min_num = min(b,min_num)
# end,cur = min_num,0
# answer = -1
# for j in range(min_num, max_num - K + 1):
#     num = 0
#     for i in range(j-K,j+K+1):
#         if ice[i] != 0:
#             num +=ice[i]

#     answer = max(answer,num)

# print(answer)  

N, K = map(int,input().split())
ice = [0] * 1000001
max_num = 0

for _ in range(N):
    a,b = map(int,input().split())
    ice[b] = a
    max_num = max(b,max_num)
size = 2 * K + 1
window = sum(ice[:size])
answer = window
for i in range(size,max_num+1):
    window += ice[i] -ice[i-size]
    answer = max(answer,window)
print(answer)