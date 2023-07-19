# # N,K= map(int,input().split())

# # num = {}

# # num_list = map(int,input().split())

# # start = 0
# # end = 0
# # # count = 0
# # answer =0
    
# # for i in num_list:
# #     if i in num:
# #         num[i] +=1
# #     else:
# #         num[i] = 1
    
# #     if num[i] <=K:
# #         end +=1
# #     else:
# #         num[start] -=1
# #         start +=1
# #     answer = max(answer,end-start)
# #     print(end,start)

# # print(answer)

# N, K = map(int, input().split())
# numbers = list(map(int, input().split()))
# left, right = 0, 0

# counter = [0] * (max(numbers) + 1)
# answer = 0
# while right < N:
#     if counter[numbers[right]] < K:
#         counter[numbers[right]] += 1
#         right += 1
#     else:
#         counter[numbers[left]] -= 1
#         left += 1
#     answer = max(answer, right - left)
# print(answer)

import sys
n, k = map(int,input().split())
num = list(map(int,sys.stdin.readline().rstrip().split()))
num_dic = [0] * ((max(num)) + 1)

start = 0
end = 0
answer = 0
while end < n:
    if num_dic[num[end]] < k:
        num_dic[num[end]] +=1
        end +=1
    else:
        num_dic[num[start]] -=1
        start +=1
    answer = max(end-start,answer)

print(answer)
    